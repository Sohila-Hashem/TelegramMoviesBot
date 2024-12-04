import random
import traceback

from telegram import Update,ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import  ContextTypes

from app.utils.utils import get_movie_response
from app.services.Movies.movies_service import MovieCategoryMap, IMovieService
from app.services.Trailers.trailer_service import  ITrailerService

class MovieServiceHandlers:
    def __init__(self, movie_service: IMovieService, trailer_service: ITrailerService) -> None:
        self.movie_service = movie_service
        self.trailer_service = trailer_service

    def suggest_movie(self, category): 
        async def suggest_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
            try:
                await update.message.reply_text(f"fetching a {category} Movie for you...🚀")
                category_id = MovieCategoryMap.get_category_id(category)
                
                category_total_pages = self.movie_service.get_page_count(category_id)
                
                random_page_num = random.randint(1, min(500, category_total_pages))

                rand_page_movies_list = self.movie_service.get_movies(category_id, random_page_num)

                if rand_page_movies_list:
                    random_movie = self.movie_service.get_random_movie(rand_page_movies_list)

                    await update.message.reply_html(get_movie_response(random_movie))

                    movie_trailers = self.trailer_service.get_movie_trailers(random_movie["id"])
                    
                    if movie_trailers:
                        filtered_movie_trailers = self.trailer_service.filter_trailers(movie_trailers, 'YouTube')

                        if filtered_movie_trailers and len(filtered_movie_trailers):
                            await update.message.reply_text("see a list of official trailers below")
                            await update.message.reply_html(f"""
                                {
                                    list(map(lambda x: f'<a href="https://www.youtube.com/watch?v={x["key"]}">{x["name"]}</a>', filtered_movie_trailers))
                                }
                        """)
                    
                    keyboard = [KeyboardButton(f"/{category}"), KeyboardButton(f"/menu")]
                    await update.message.reply_text('Suggest another movie?', reply_markup=ReplyKeyboardMarkup([keyboard], resize_keyboard=True))
                    return
                
                await update.message.reply_text("No movies were found for this category")
            except Exception as e:
                print(f"something went wrong while executing suggest_movie_command: {traceback.format_exception(type(e), value=e, tb=e.__traceback__)}")
                await update.message.reply_text("Something went wrong. Please try again later :(")

        return suggest_movie_command