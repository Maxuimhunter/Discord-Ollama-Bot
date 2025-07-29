# Discord Ollama Bot

A Discord bot that integrates with Ollama to provide AI-powered chat capabilities. This bot can be used to interact with various language models hosted on an Ollama instance directly from Discord.

## Features

- Seamless integration with Ollama's API
- Support for multiple AI models (default: gemma3)
- Simple mention-based interaction
- Admin commands for model management
- Typing indicators for better user experience
- Environment-based configuration

## Prerequisites

Before you begin, ensure you have the following:

1. Python 3.8 or higher
2. An Ollama server running (default: http://localhost:11434)
3. A Discord bot token
4. Required Python packages (see Installation)

## Installation

1. Clone this repository or download the source code
2. Install the required Python packages:
   ```bash
   pip install discord.py python-dotenv aiohttp
   ```
3. Create a `.env` file in the project directory with the following content:
   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   OLLAMA_BASE_URL=http://localhost:11434  # Change if your Ollama is running elsewhere
   OLLAMA_MODEL=gemma3  # Default model to use
   ```
   Replace `your_discord_bot_token_here` with your actual Discord bot token.

## Running the Bot

1. Ensure your Ollama server is running
2. Run the bot using Python:
   ```bash
   python discord_ollama_bot.py
   ```
3. The bot should now be online in your Discord server

## Usage

### Basic Usage
- Mention the bot in any channel it has access to, followed by your message:
  ```
  @BotName Hello, how are you?
  ```
- The bot will respond to your message in the same channel

### Available Commands
- `!ping` - Check if the bot is responsive
- `!setmodel <model_name>` (Admin only) - Change the Ollama model being used

## Integration with a Discord Bot

### Creating a Discord Bot
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click on "New Application" and give it a name
3. Navigate to the "Bot" tab and click "Add Bot"
4. Under the Bot tab, copy the token (this is your `DISCORD_TOKEN`)
5. Under OAuth2 > URL Generator, select `bot` and `applications.commands` scopes
6. Under Bot Permissions, select:
   - Send Messages
   - Read Messages/View Channels
   - Use External Emojis
   - Add Reactions
   - Use Slash Commands
7. Use the generated URL to add the bot to your server

### Adding the Bot to Your Server
1. Use the OAuth2 URL generated in the previous step
2. Select the server you want to add the bot to
3. Authorize the bot with the selected permissions

## Configuration

You can customize the bot's behavior by modifying the following environment variables in your `.env` file:

- `DISCORD_TOKEN`: Your Discord bot token (required)
- `OLLAMA_BASE_URL`: URL of your Ollama server (default: http://localhost:11434)
- `OLLAMA_MODEL`: Default model to use (default: gemma3)

## Troubleshooting

- **Bot not responding**:
  - Check if the bot is running
  - Verify the bot has the correct permissions in the channel
  - Ensure the bot is mentioned correctly

- **Ollama connection issues**:
  - Verify Ollama server is running and accessible
  - Check the `OLLAMA_BASE_URL` in your `.env` file
  - Ensure the specified model is available on your Ollama instance

## Security Note

Keep your `.env` file secure and never commit it to version control. The `.env` file is included in `.gitignore` by default.

## License

This project is open source and available under the [MIT License](LICENSE).
