import logging
from typing import Dict
import telebot
from movie_service import MovieService
from config import TELEGRAM_BOT_TOKEN, MAX_SEARCH_RESULTS

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class MovieBot:
    """Telegram bot for movie search functionality using pyTelegramBotAPI"""
    
    def __init__(self):
        self.movie_service = MovieService()
        self.bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
        self.setup_handlers()
    
    def setup_handlers(self) -> None:
        """Setup command and message handlers."""
        
        @self.bot.message_handler(commands=['start'])
        def start(message):
            """Send a message when the command /start is issued."""
            welcome_message = (
                "🎬 *Welcome to Movie Search Bot!*\n\n"
                "I can help you search for movies and get detailed information including posters.\n\n"
                "*Available Commands:*\n"
                "• `/search <movie_title>` - Search for movies\n"
                "• `/details <imdb_id>` - Get detailed movie information\n"
                "• `/help` - Show this help message\n\n"
                "*Examples:*\n"
                "• `/search The Dark Knight`\n"
                "• `/details tt0468569`\n\n"
                "Just type a movie name to search quickly! 🍿"
            )
            
            self.bot.reply_to(message, welcome_message, parse_mode='Markdown')
        
        @self.bot.message_handler(commands=['help'])
        def help_command(message):
            """Send a message when the command /help is issued."""
            help_message = (
                "🎬 *Movie Search Bot Help*\n\n"
                "*Commands:*\n"
                "• `/start` - Start the bot and see welcome message\n"
                "• `/search <movie_title>` - Search for movies by title\n"
                "• `/details <imdb_id>` - Get detailed information about a movie\n"
                "• `/help` - Show this help message\n\n"
                "*Quick Search:*\n"
                "You can also just type a movie name without any command to search!\n\n"
                "*Examples:*\n"
                "• `Inception`\n"
                "• `/search Avatar`\n"
                "• `/details tt1375666`\n\n"
                "*Tips:*\n"
                "• Use specific movie titles for better results\n"
                "• Copy the IMDb ID from search results to get full details\n"
                "• Movie posters will be shown when available\n\n"
                "Happy movie searching! 🍿"
            )
            
            self.bot.reply_to(message, help_message, parse_mode='Markdown')
        
        @self.bot.message_handler(commands=['search'])
        def search_movies(message):
            """Handle movie search command."""
            # Get the search query from the message text
            query = message.text.replace('/search', '').strip()
            
            if not query:
                self.bot.reply_to(
                    message,
                    "❌ Please provide a movie title to search.\n"
                    "Example: `/search The Dark Knight`",
                    parse_mode='Markdown'
                )
                return
            
            self._perform_search(message, query)
        
        @self.bot.message_handler(commands=['details'])
        def get_movie_details(message):
            """Handle movie details command."""
            # Get the IMDb ID from the message text
            imdb_id = message.text.replace('/details', '').strip()
            
            if not imdb_id:
                self.bot.reply_to(
                    message,
                    "❌ Please provide an IMDb ID to get movie details.\n"
                    "Example: `/details tt0468569`",
                    parse_mode='Markdown'
                )
                return
            
            self._get_details(message, imdb_id)
        
        @self.bot.message_handler(func=lambda message: True)
        def handle_text_search(message):
            """Handle text messages as movie searches."""
            query = message.text.strip()
            
            # Ignore very short queries
            if len(query) < 2:
                self.bot.reply_to(
                    message,
                    "🔍 Please provide a longer movie title for better search results."
                )
                return
            
            self._perform_search(message, query)
    
    def _perform_search(self, message, query: str) -> None:
        """Perform movie search and send results."""
        # Send typing action
        self.bot.send_chat_action(message.chat.id, 'typing')
        
        try:
            # Search for movies
            search_results = self.movie_service.search_movies(query)
            formatted_results = self.movie_service.format_search_results(search_results)
            
            self.bot.reply_to(
                message,
                formatted_results,
                parse_mode='Markdown'
            )
            
        except Exception as e:
            logger.error(f"Error in movie search: {str(e)}")
            self.bot.reply_to(
                message,
                "❌ Sorry, there was an error processing your search. Please try again later."
            )
    
    def _get_details(self, message, imdb_id: str) -> None:
        """Get detailed movie information and send response."""
        # Send typing action
        self.bot.send_chat_action(message.chat.id, 'typing')
        
        try:
            # Get movie details
            movie_details = self.movie_service.get_movie_details(imdb_id=imdb_id)
            
            if movie_details.get('Response') == 'False':
                self.bot.reply_to(
                    message,
                    f"❌ {movie_details.get('Error', 'Movie not found.')}"
                )
                return
            
            # Format movie details
            formatted_details = self.movie_service.format_movie_details(movie_details)
            
            # Get poster URL
            poster_url = movie_details.get('Poster', '')
            
            # Send movie details with poster if available
            if poster_url and poster_url != 'N/A':
                try:
                    self.bot.send_photo(
                        message.chat.id,
                        photo=poster_url,
                        caption=formatted_details,
                        parse_mode='Markdown'
                    )
                except Exception as e:
                    logger.warning(f"Failed to send poster: {str(e)}")
                    # Send text only if poster fails
                    self.bot.reply_to(
                        message,
                        formatted_details,
                        parse_mode='Markdown'
                    )
            else:
                self.bot.reply_to(
                    message,
                    formatted_details,
                    parse_mode='Markdown'
                )
                
        except Exception as e:
            logger.error(f"Error getting movie details: {str(e)}")
            self.bot.reply_to(
                message,
                "❌ Sorry, there was an error getting movie details. Please try again later."
            )
    
    def run(self) -> None:
        """Start the bot."""
        logger.info("Movie Bot is starting...")
        
        try:
            # Start the bot polling
            self.bot.polling(non_stop=True, interval=0)
        except Exception as e:
            logger.error(f"Error running bot: {str(e)}")
            raise
