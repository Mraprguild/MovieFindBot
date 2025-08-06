import requests
import json
from typing import Dict, List, Optional
from config import OMDB_API_KEY, OMDB_BASE_URL, TIMEOUT_SECONDS

class MovieService:
    """Service class to handle OMDB API interactions"""
    
    def __init__(self):
        self.api_key = OMDB_API_KEY
        self.base_url = OMDB_BASE_URL
        
    def search_movies(self, query: str, page: int = 1) -> Dict:
        """
        Search for movies by title
        
        Args:
            query (str): Movie title to search for
            page (int): Page number for pagination
            
        Returns:
            Dict: API response containing search results
        """
        try:
            params = {
                'apikey': self.api_key,
                's': query,
                'page': page,
                'type': 'movie'
            }
            
            response = requests.get(
                self.base_url,
                params=params,
                timeout=TIMEOUT_SECONDS
            )
            response.raise_for_status()
            
            data = response.json()
            return data
            
        except requests.exceptions.RequestException as e:
            return {
                'Response': 'False',
                'Error': f'Network error: {str(e)}'
            }
        except json.JSONDecodeError as e:
            return {
                'Response': 'False',
                'Error': 'Invalid response format from API'
            }
        except Exception as e:
            return {
                'Response': 'False',
                'Error': f'Unexpected error: {str(e)}'
            }
    
    def get_movie_details(self, imdb_id: Optional[str] = None, title: Optional[str] = None) -> Dict:
        """
        Get detailed information about a specific movie
        
        Args:
            imdb_id (str): IMDb ID of the movie
            title (str): Title of the movie
            
        Returns:
            Dict: Detailed movie information
        """
        try:
            params = {
                'apikey': self.api_key,
                'plot': 'full'
            }
            
            if imdb_id:
                params['i'] = imdb_id
            elif title:
                params['t'] = title
            else:
                return {
                    'Response': 'False',
                    'Error': 'Either IMDb ID or title must be provided'
                }
            
            response = requests.get(
                self.base_url,
                params=params,
                timeout=TIMEOUT_SECONDS
            )
            response.raise_for_status()
            
            data = response.json()
            return data
            
        except requests.exceptions.RequestException as e:
            return {
                'Response': 'False',
                'Error': f'Network error: {str(e)}'
            }
        except json.JSONDecodeError as e:
            return {
                'Response': 'False',
                'Error': 'Invalid response format from API'
            }
        except Exception as e:
            return {
                'Response': 'False',
                'Error': f'Unexpected error: {str(e)}'
            }
    
    def escape_markdown(self, text: str) -> str:
        """Escape markdown special characters"""
        if not text or text == 'N/A':
            return text
        # Escape common markdown characters that cause parsing issues
        escape_chars = ['*', '_', '`', '[', ']', '(', ')', '~', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
        for char in escape_chars:
            text = text.replace(char, f'\\{char}')
        return text

    def format_movie_details(self, movie_data: Dict) -> str:
        """
        Format movie details for display
        
        Args:
            movie_data (Dict): Movie data from OMDB API
            
        Returns:
            str: Formatted movie information
        """
        if movie_data.get('Response') == 'False':
            return f"❌ Error: {movie_data.get('Error', 'Unknown error occurred')}"
        
        # Extract movie information and escape markdown
        title = self.escape_markdown(movie_data.get('Title', 'N/A'))
        year = movie_data.get('Year', 'N/A')
        genre = self.escape_markdown(movie_data.get('Genre', 'N/A'))
        director = self.escape_markdown(movie_data.get('Director', 'N/A'))
        actors = self.escape_markdown(movie_data.get('Actors', 'N/A'))
        plot = self.escape_markdown(movie_data.get('Plot', 'N/A'))
        imdb_rating = movie_data.get('imdbRating', 'N/A')
        runtime = movie_data.get('Runtime', 'N/A')
        language = self.escape_markdown(movie_data.get('Language', 'N/A'))
        country = self.escape_markdown(movie_data.get('Country', 'N/A'))
        awards = self.escape_markdown(movie_data.get('Awards', 'N/A'))
        
        # Format the message
        message = f"🎬 *{title}* ({year})\n\n"
        message += f"📝 *Plot:* {plot}\n\n"
        message += f"🎭 *Genre:* {genre}\n"
        message += f"🎬 *Director:* {director}\n"
        message += f"👥 *Actors:* {actors}\n"
        message += f"⭐ *IMDb Rating:* {imdb_rating}/10\n"
        message += f"⏱️ *Runtime:* {runtime}\n"
        message += f"🌍 *Language:* {language}\n"
        message += f"🏁 *Country:* {country}\n"
        
        if awards != 'N/A':
            message += f"🏆 *Awards:* {awards}\n"
        
        return message
    
    def format_search_results(self, search_data: Dict) -> str:
        """
        Format search results for display
        
        Args:
            search_data (Dict): Search results from OMDB API
            
        Returns:
            str: Formatted search results
        """
        if search_data.get('Response') == 'False':
            return f"❌ {search_data.get('Error', 'No movies found matching your search.')}"
        
        movies = search_data.get('Search', [])
        if not movies:
            return "❌ No movies found matching your search."
        
        message = f"🔍 *Search Results* (Found {search_data.get('totalResults', len(movies))} movies):\n\n"
        
        for i, movie in enumerate(movies[:5], 1):  # Limit to first 5 results
            title = self.escape_markdown(movie.get('Title', 'N/A'))
            year = movie.get('Year', 'N/A')
            imdb_id = movie.get('imdbID', '')
            
            message += f"{i}\\. *{title}* ({year})\n"
            message += f"   IMDb ID: `{imdb_id}`\n\n"
        
        message += "💡 Use /details <IMDb\\_ID> to get full details of any movie\\."
        
        return message
