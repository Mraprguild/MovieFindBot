# Movie Search Telegram Bot

## Overview

This is a fully operational Telegram bot that provides comprehensive movie search functionality using the OMDB (Open Movie Database) API. Users can search for movies by title and get detailed information including posters, ratings, plot summaries, and other metadata. The bot supports both quick text-based searches and detailed movie information retrieval using IMDb IDs.

## Recent Changes (August 6, 2025)

- ✅ **CRITICAL FIX: Resolved telegram library import issues**
- ✅ Migrated from broken python-telegram-bot to pyTelegramBotAPI
- ✅ Bot now running successfully with stable imports and functionality
- ✅ All commands (/start, /help, /search, /details) verified working
- ✅ Movie service integration tested and confirmed (OMDB API working)
- ✅ Comprehensive rewrite using pyTelegramBotAPI's simplified syntax
- ✅ Error handling and logging maintained during library migration
- ✅ Bot workflow status: RUNNING (no import errors)

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Bot Framework
- **Telegram Bot API**: Uses pyTelegramBotAPI library (telebot) for handling Telegram interactions
- **Command-based Interface**: Supports `/start`, `/help`, `/search`, and `/details` commands
- **Message Handlers**: Processes both command and text messages for flexible user interaction
- **Library Choice**: Migrated to pyTelegramBotAPI for better stability and reliability

### Service Layer Architecture
- **MovieService Class**: Encapsulates all OMDB API interactions
- **Separation of Concerns**: Bot logic separated from movie data retrieval
- **Error Handling**: Comprehensive error handling for network issues and API failures
- **Timeout Management**: Configurable timeout settings for API requests

### Configuration Management
- **Environment Variables**: Sensitive data (API keys, bot tokens) stored as environment variables
- **Centralized Config**: Single configuration file for all settings and constants
- **Default Values**: Fallback values provided for development ease

### Data Flow
- **Stateless Design**: No persistent data storage, all interactions are request-response based
- **JSON Processing**: Direct JSON parsing from OMDB API responses
- **Media Handling**: Support for displaying movie posters via Telegram's media capabilities

### Error Handling Strategy
- **Graceful Degradation**: Bot continues functioning even when API calls fail
- **User-Friendly Messages**: API errors translated to readable messages for users
- **Logging**: Comprehensive logging for debugging and monitoring

## External Dependencies

### APIs
- **OMDB API**: Primary data source for movie information, requires API key authentication
- **Telegram Bot API**: For bot functionality, requires bot token from @BotFather

### Python Libraries
- **pyTelegramBotAPI**: Telegram bot framework and API wrapper (replaced python-telegram-bot)
- **requests**: HTTP client for OMDB API calls
- **logging**: Built-in logging for application monitoring
- **telebot**: Simple and stable Telegram Bot API wrapper

### Environment Requirements
- **TELEGRAM_BOT_TOKEN**: Bot authentication token from Telegram
- **OMDB_API_KEY**: API key for accessing movie database
- **Python 3.x**: Runtime environment with async/await support