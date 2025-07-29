import os
import discord
from discord.ext import commands
import aiohttp
import json
import logging
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('discord_ollama_bot')

# Configuration
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'gemma3')

# Set up Discord bot with intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

class OllamaClient:
    def __init__(self, base_url: str = OLLAMA_BASE_URL):
        self.base_url = base_url
        self.session = None

    async def ensure_session(self):
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()

    async def generate_response(self, prompt: str, model: str = OLLAMA_MODEL) -> Optional[str]:
        """Generate a response from Ollama"""
        url = f"{self.base_url}/api/generate"
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": False
        }

        try:
            await self.ensure_session()
            async with self.session.post(url, json=payload) as response:
                if response.status == 200:
                    result = await response.json()
                    return result.get('response', 'No response generated')
                else:
                    error_text = await response.text()
                    logger.error(f"Ollama API error: {response.status} - {error_text}")
                    return None
        except Exception as e:
            logger.error(f"Error communicating with Ollama: {str(e)}")
            return None

# Initialize Ollama client
ollama_client = OllamaClient()

@bot.event
async def on_ready():
    """Event triggered when the bot is ready"""
    logger.info(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    logger.info('------')
    await bot.change_presence(activity=discord.Game(name="with Ollama"))

@bot.event
async def on_message(message):
    """Handle incoming messages"""
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Process commands first
    await bot.process_commands(message)
    
    # Skip if message is empty, just contains whitespace, or doesn't mention the bot
    if not message.content.strip() or bot.user not in message.mentions:
        return
        
    # Show typing indicator
    async with message.channel.typing():
        try:
            # Remove the bot mention from the message
            clean_content = message.content.replace(f'<@{bot.user.id}>', '').strip()
            
            # Skip if message only contains the bot mention
            if not clean_content:
                return
                
            # Get response from Ollama
            response = await ollama_client.generate_response(clean_content)
            
            if response:
                # Mention the user who sent the message
                mention = f"{message.author.mention} "
                full_response = f"{mention}{response}"
                
                # Split long messages to respect Discord's 2000 character limit
                if len(full_response) > 1900:
                    chunks = [full_response[i:i+1900] for i in range(0, len(full_response), 1900)]
                    for chunk in chunks:
                        await message.channel.send(chunk)
                else:
                    await message.channel.send(full_response)
            else:
                await message.channel.send(f"{message.author.mention} Sorry, I couldn't generate a response at the moment.")
        except Exception as e:
            logger.error(f"Error generating response: {str(e)}")
            await message.channel.send(f"{message.author.mention} An error occurred while processing your message.")

@bot.command(name='ping')
async def ping(ctx):
    """Simple command to check if the bot is alive"""
    await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')

@bot.command(name='setmodel')
@commands.has_permissions(administrator=True)
async def set_model(ctx, model_name: str):
    """Command to change the Ollama model (Admin only)"""
    global OLLAMA_MODEL
    OLLAMA_MODEL = model_name
    await ctx.send(f'Ollama model set to: {model_name}')

@bot.event
async def on_command_error(ctx, error):
    """Handle command errors"""
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command.")
    elif isinstance(error, commands.CommandNotFound):
        pass  # Ignore unknown commands
    else:
        logger.error(f'Error in command {ctx.command}: {str(error)}')
        await ctx.send("An error occurred while processing the command.")

def main():
    """Run the bot"""
    if not DISCORD_TOKEN:
        logger.error("No Discord token provided. Please set the DISCORD_TOKEN environment variable.")
        return

    try:
        bot.run(DISCORD_TOKEN)
    except Exception as e:
        logger.error(f"Error starting bot: {str(e)}")
    finally:
        # Clean up
        if ollama_client.session and not ollama_client.session.closed:
            bot.loop.run_until_complete(ollama_client.session.close())

if __name__ == "__main__":
    main()
