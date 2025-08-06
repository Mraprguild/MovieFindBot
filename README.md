# 🎬 Telegram Movie Search Bot

A comprehensive Telegram bot that provides movie search functionality using the OMDB API, complete with poster images and detailed information.

## Features

- 🔍 **Movie Search**: Search for movies by title
- 🖼️ **Movie Posters**: Display movie poster images
- 📋 **Detailed Information**: Get comprehensive movie details including plot, cast, ratings
- 🤖 **Interactive Commands**: Support for /start, /help, /search, /details
- ⚡ **Quick Search**: Just type a movie name to search instantly
- 📊 **Web Dashboard**: Monitor bot status and statistics
- 🐳 **Docker Support**: Easy deployment with Docker

## Quick Start

### Using Docker (Recommended)

1. Clone the repository
2. Copy environment file and configure API keys:
   ```bash
   cp .env.example .env
   nano .env
   ```
3. Build and run:
   ```bash
   chmod +x build.sh
   ./build.sh
   docker-compose up -d
   ```

### Manual Setup

1. Install dependencies:
   ```bash
   pip install python-telegram-bot requests flask psutil
   ```

2. Set environment variables:
   ```bash
   export TELEGRAM_BOT_TOKEN="your_bot_token"
   export OMDB_API_KEY="your_omdb_key"
   ```

3. Run the bot:
   ```bash
   python main.py
   ```

## Getting API Keys

### Telegram Bot Token
1. Open Telegram and search for @BotFather
2. Start a chat and type `/newbot`
3. Follow instructions to create your bot
4. Copy the token you receive

### OMDB API Key
1. Visit [http://www.omdbapi.com/apikey.aspx](http://www.omdbapi.com/apikey.aspx)
2. Sign up for a free account
3. Copy your API key from the confirmation email

## Bot Commands

- `/start` - Start the bot and see welcome message
- `/help` - Show help message and usage instructions
- `/search <movie_title>` - Search for movies by title
- `/details <imdb_id>` - Get detailed movie information
- **Quick Search** - Just type any movie name to search instantly

## Web Dashboard

Access the web dashboard at `http://localhost:5000` to monitor:
- Bot status and uptime
- API service status
- Usage statistics
- Available commands

## Docker Commands

```bash
# Build the image
docker build -t telegram-movie-bot .

# Run with docker-compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the bot
docker-compose down

# Rebuild and restart
docker-compose up -d --build
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `TELEGRAM_BOT_TOKEN` | Your Telegram bot token from @BotFather | Yes |
| `OMDB_API_KEY` | Your OMDB API key | Yes |
| `FLASK_ENV` | Flask environment (production/development) | No |
| `PORT` | Web dashboard port (default: 5000) | No |

## File Structure

```
├── bot.py                 # Main bot logic
├── config.py              # Configuration settings
├── main.py                # Bot entry point
├── movie_service.py       # OMDB API service
├── web_server.py          # Web dashboard
├── run_with_dashboard.py  # Combined startup script
├── templates/
│   └── index.html         # Dashboard template
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose setup
└── docker-requirements.txt # Python dependencies
```

## Health Check

The bot includes a health check endpoint at `/health` for monitoring:

```bash
curl http://localhost:5000/health
```

## Troubleshooting

### Common Issues

1. **Import errors**: Make sure all dependencies are installed
2. **API errors**: Verify your API keys are correct
3. **Port conflicts**: Change the port in docker-compose.yml if needed

### Viewing Logs

```bash
# Docker logs
docker-compose logs -f movie-bot

# Direct execution logs
python main.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For support, please create an issue in the repository or contact the maintainers.