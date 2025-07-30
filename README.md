# 🤖 Discord Ollama Bot

Welcome to the Discord Ollama Bot! This bot brings the power of Ollama's language models directly into your Discord server, allowing you to have AI-powered conversations with just a mention.

## ✨ Features

- **AI-Powered Chat**: Have natural conversations with various language models
- **Multiple Model Support**: Easily switch between different Ollama models
- **User-Friendly**: Simple mention-based interaction - just @ the bot and type your message
- **Admin Controls**: Special commands for server administrators
- **Real-time Feedback**: Typing indicators show when the bot is generating a response
- **Customizable**: Configure settings through environment variables

## 🚀 Quick Start Guide

### Prerequisites

Before we begin, make sure you have:

1. **Python 3.8 or higher**
   - [Download Python](https://www.python.org/downloads/)
   - Verify installation: `python --version`

2. **Ollama Server**
   - [Install Ollama](https://ollama.ai/)
   - Start the server: `ollama serve` (keep this running in a separate terminal)
   - Pull a model: `ollama pull gemma3`

3. **Discord Bot Token**
   - We'll create this in the setup steps below

## 🛠 Installation

### Step 1: Get the Code

```bash
# Clone this repository
git clone https://github.com/yourusername/discord-ollama-bot.git
cd discord-ollama-bot
```

### Step 2: Set Up Python Environment

```bash
# Create a virtual environment (recommended)
python -m venv venv

# Activate the virtual environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### Step 3: Configure Your Bot

1. **Create a Discord Bot**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application" and name it (e.g., "Ollama Bot")
   - Navigate to "Bot" in the left sidebar
   - Click "Add Bot" and confirm
   - Under "TOKEN", click "Copy" - this is your `DISCORD_TOKEN`
   
2. **Set Up Permissions**
   - Go to "OAuth2" > "URL Generator"
   - Check `bot` and `applications.commands` in Scopes
   - In Bot Permissions, enable:
     - Read Messages/View Channels
     - Send Messages
     - Read Message History
     - Use External Emojis
     - Add Reactions
   - Copy the generated URL and open it in your browser
   - Select your server and authorize the bot

3. **Configure Environment**
   - Create a new file named `.env` in the project directory
   - Add the following content:
     ```
     # Your Discord bot token from the Developer Portal
     DISCORD_TOKEN=your_discord_bot_token_here
     
     # Ollama server URL (default is usually fine)
     OLLAMA_BASE_URL=http://localhost:11434
     
     # Default model to use (must be installed in Ollama)
     OLLAMA_MODEL=gemma3
     ```
   - Replace `your_discord_bot_token_here` with the token you copied earlier

## 🚀 Running the Bot

1. **Start Ollama Server** (if not already running)
   ```bash
   # In a new terminal window
   ollama serve
   ```

2. **Start the Discord Bot**
   ```bash
   # Make sure your virtual environment is activated
   python discord_ollama_bot.py
   ```

3. **Verify the Bot is Online**
   - Check your Discord server - the bot should appear online
   - Try mentioning the bot in any channel: `@BotName Hello!`

## 🤖 Using the Bot

### Basic Commands
- **Chat with the bot**: Just mention it in any channel
  ```
  @BotName What's the weather like today?
  ```

### Admin Commands
- `!ping` - Check if the bot is responding
- `!setmodel <model_name>` - Change the Ollama model (admin only)
  Example: `!setmodel llama2`

## ⚙️ Configuration Options

Edit the `.env` file to customize:

| Variable | Description | Default |
|----------|-------------|---------|
| `DISCORD_TOKEN` | Your bot's secret token | (required) |
| `OLLAMA_BASE_URL` | URL of your Ollama server | `http://localhost:11434` |
| `OLLAMA_MODEL` | Default model to use | `gemma3` |

## 🔍 Troubleshooting

### Bot Not Responding?
1. **Check Bot Status**
   - Is the bot script running without errors?
   - Is the bot online in your server?
   
2. **Verify Permissions**
   - Does the bot have permission to read/send messages in the channel?
   - Is the bot mentioned correctly? Try copying the mention from Discord's user list

3. **Ollama Connection Issues**
   - Is Ollama server running? Try `curl http://localhost:11434/api/tags`
   - Is the model downloaded? Run `ollama list` to check
   - Check the bot's console for error messages

### Common Errors
- **"Invalid token"**: Double-check your `DISCORD_TOKEN` in `.env`
- **"Connection refused"**: Make sure Ollama server is running
- **"Model not found"**: The specified model isn't installed. Try `ollama pull gemma3`

## 🔒 Security Best Practices

1. **Never share your bot token**
   - The `.env` file is automatically ignored by Git
   - If you accidentally commit it, rotate the token immediately

2. **Bot Permissions**
   - Only grant necessary permissions
   - Consider creating a separate Discord server for testing

3. **Regular Updates**
   - Keep your dependencies updated:
     ```bash
     pip install --upgrade -r requirements.txt
     ```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
## 🙏 Acknowledgments

- [Ollama](https://ollama.ai/) for the powerful language models
- [discord.py](https://discordpy.readthedocs.io/) for the Discord API wrapper
