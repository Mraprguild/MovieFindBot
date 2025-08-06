import os

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "your_telegram_bot_token")

# OMDB API Configuration
OMDB_API_KEY = os.getenv("OMDB_API_KEY", "your_omdb_api_key")
OMDB_BASE_URL = "http://www.omdbapi.com/"

# Bot Settings
MAX_SEARCH_RESULTS = 5
TIMEOUT_SECONDS = 30
