from telegram import Update
from telegram.ext import  ContextTypes

from utils import get_menu, get_random_movie, get_movie_trailers, display_response, display_after_response_menu

supported_movie_categories: dict[str, int] = {
    "Action": 28,
    "Adventure": 12,
    "Animation": 16,
    "Comedy": 35,
    "Crime": 80,
    "Documentary": 99,
    "Drama": 18,
    "Family": 10751,
    "Fantasy": 14,
    "History": 36,
    "Horror": 27,
    "Music": 10402,
    "Mystery": 9648,
    "Romance": 10749,
    "Science Fiction": 878,
    "TV Movie": 10770,
    "Thriller": 53,
    "War": 10752,
    "Western": 37,
}


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = get_menu()
    await update.message.reply_text("Welcome to Movies4U bot, What's your Movie choice today 😀?", reply_markup=reply_markup)

async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = get_menu()
    await update.message.reply_text("What's your Movie choice today 😀?", reply_markup=reply_markup)

async def suggest_action_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting an Action Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Action"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)

async def suggest_adventure_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting an Adventure Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Adventure"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)


async def suggest_animation_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting an Animation Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Animation"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)


async def suggest_comedy_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a Comedy Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Comedy"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)


async def suggest_crime_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a Crime Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Crime"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)


async def suggest_documentary_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a Documentary Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Documentary"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)


async def suggest_drama_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a Drama Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Drama"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)


async def suggest_family_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a Family Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Family"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)


async def suggest_fantasy_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a Fantasy Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Fantasy"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)


async def suggest_history_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a History Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["History"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)


async def suggest_horror_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a Horror Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Horror"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)


async def suggest_music_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a Music Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Music"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)

async def suggest_mystery_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a Mystery Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Mystery"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)

async def suggest_romance_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a Romance Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Romance"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)

async def suggest_sci_fi_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a Science Fiction Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Science Fiction"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)

async def suggest_thriller_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a Thriller Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Thriller"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)

async def suggest_tv_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a TV Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["TV Movie"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)

async def suggest_war_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a War Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["War"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)

async def suggest_western_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Suggesting a Western Movie for you...🚀")

    movie = get_random_movie(supported_movie_categories["Western"])

    await display_response(movie, update)

    movie_trailer_key = get_movie_trailers(movie["id"])

    await display_after_response_menu(movie_trailer_key, update)
