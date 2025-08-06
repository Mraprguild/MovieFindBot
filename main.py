#!/usr/bin/env python3
"""
Telegram Movie Search Bot

A Telegram bot that searches for movies using the OMDB API and displays
detailed information including poster images.

Usage:
    python main.py

Environment Variables Required:
    - TELEGRAM_BOT_TOKEN: Your Telegram bot token from @BotFather
    - OMDB_API_KEY: Your OMDB API key from http://www.omdbapi.com/

Commands:
    /start - Start the bot
    /help - Show help message
    /search <movie_title> - Search for movies
    /details <imdb_id> - Get detailed movie information
"""

import sys
import logging
from bot import MovieBot
from config import TELEGRAM_BOT_TOKEN, OMDB_API_KEY

def main():
    """Main function to start the movie bot."""
    
    # Configure logging
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        handlers=[
            logging.StreamHandler(sys.stdout),
        ]
    )
    
    logger = logging.getLogger(__name__)
    
    # Check if required environment variables are set
    if TELEGRAM_BOT_TOKEN == "your_telegram_bot_token":
        logger.error("TELEGRAM_BOT_TOKEN environment variable not set!")
        logger.error("Please set your Telegram bot token from @BotFather")
        sys.exit(1)
    
    if OMDB_API_KEY == "your_omdb_api_key":
        logger.error("OMDB_API_KEY environment variable not set!")
        logger.error("Please get your API key from http://www.omdbapi.com/")
        sys.exit(1)
    
    logger.info("Starting Telegram Movie Search Bot...")
    logger.info("Bot token configured: ✓")
    logger.info("OMDB API key configured: ✓")
    
    try:
        # Create and start the bot
        bot = MovieBot()
        bot.run()
        
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
