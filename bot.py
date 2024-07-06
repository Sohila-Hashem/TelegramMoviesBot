import os
import random
import requests
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()

# generic variables
bot_token = os.getenv("BOT_API_TOKEN")
bot_username = os.getenv("BOT_USERNAME")
movies_api_key = os.getenv("MOVIES_API_KEY")
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


# utils
async def display_response(movie: dict, update: Update) -> None:
    await update.message.reply_html(f"How about <b>'{movie["title"]}'?</b>")
    await update.message.reply_html(f"<b>Description</b>:\n{movie["overview"]}")
    await update.message.reply_html(f"<b>Rating: {movie["vote_average"]}</b>")
    await update.message.reply_html(f"<b>Release Date: {movie["release_date"]}</b>")
    await update.message.reply_html(f"<b>Original Language: {movie["original_language"]}</b>")


async def display_after_response_menu(trailer: list | None, update: Update):
    if trailer != None:
        sub_menu = [
            [KeyboardButton("Watch Trailer", web_app=WebAppInfo(f"https://www.youtube.com/watch?v={trailer[0]["key"]}"))],
            ["/menu"],
        ]
    else:
        sub_menu = [
            ["/menu"],
        ]
    await update.message.reply_text("What else can i help you with?", reply_markup=ReplyKeyboardMarkup(sub_menu, one_time_keyboard=True))

def get_menu() -> str:
    menu = [    
        ['/horror', '/animation', ],
        ['/action', '/drama'],
        ['/romance', '/thriller'],
        ['/fantasy', '/documentary'],
        ['/mystery', '/war'],
        ['/western', '/sciencefiction'],
        ['/crime', '/tvmovie'],
        ['/adventure', '/history'],
        ['/family', '/music'],
        ['/comedy'],
    ]
    
    return ReplyKeyboardMarkup(menu, one_time_keyboard=True)

def get_movie_trailers(movie_id: int) -> list:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={movies_api_key}"

    headers = {
        "accept": "application/json",
    }

    data = requests.get(url, headers=headers).json()

    if "results" not in data:
        return None
    elif len(data["results"]) == 0:
        return None
    else:
        return data["results"]

def get_movies(category_id: int, page) -> list:
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={movies_api_key}"

    req_query_params = {
        "include_adult": "false",
        "include_video": "false",
        "language": "en-US",
        "sort_by": "popularity.desc",
        "page": page,
        "with_genres": category_id,
        "vote_average.gte": 6,
        "release_date.gte":"2010-01-01"
    }

    headers = {
        "accept": "application/json",
    }

    data = requests.get(url, headers=headers, params=req_query_params).json()

    if "results" not in data:
        return []

    return data

def get_random_movie(category_id: int) -> list:
    # we need to make a first request to get the available number of pages
    num_of_pages = get_movies(category_id, 1)["total_pages"]

    random_page = random.randint(0, min(num_of_pages, 500)) # 500 is the maximum number of pages for the API
    
    movies_list = get_movies(category_id, random_page)["results"]

    random_movie_num = random.randint(0, len(movies_list) - 1)

    return movies_list[random_movie_num]

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


# Text Responses
def handle_response(text: str) -> str:
    processed_text = text.lower()

    if 'hello' in processed_text:
        return 'Hey there!'
    
    if 'bye' in processed_text:
        return 'Looking forward to see you again, Wish you a good day!'
    
    if 'how are you' in processed_text:
        return 'All good, thanks, and you?'
    
    return "I didn't get that. Can you please rephrase?"


# Message Handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # whether the sender is sending from a private or a group chat
    message_type: str = update.message.chat.type
    text: str = update.message.text

    if message_type == 'group':
        # this is step is necessary because the bot listens for any typed messages
        # hence we only need to respond when it's specifically called by the it's name
        if bot_username in text:
            text = text.replace(bot_username, '').strip()
            response: str = handle_response(text)
        else:
            return
    # we respond directly to the message as the sender is communicating directly with the bot privately
    else :
        response: str = handle_response(text)

    # print(f'Bot sent: "{response}"')
    await update.message.reply_text(response)

# Error Handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'Update "{update}"\n caused error "{context.error}"')

if __name__ == '__main__':
    print('Starting bot...')

    app = ApplicationBuilder().token(bot_token).build()

    # adding handlers for commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('menu', menu_command))
    app.add_handler(CommandHandler('horror', suggest_horror_movie_command))
    app.add_handler(CommandHandler('animation', suggest_animation_movie_command))
    app.add_handler(CommandHandler('comedy', suggest_comedy_movie_command))
    app.add_handler(CommandHandler('action', suggest_action_movie_command))
    app.add_handler(CommandHandler('drama', suggest_drama_movie_command))
    app.add_handler(CommandHandler('family', suggest_family_movie_command))
    app.add_handler(CommandHandler('fantasy', suggest_fantasy_movie_command))
    app.add_handler(CommandHandler('history', suggest_history_movie_command))
    app.add_handler(CommandHandler('adventure', suggest_adventure_movie_command))
    app.add_handler(CommandHandler('music', suggest_music_movie_command))
    app.add_handler(CommandHandler('mystery', suggest_mystery_movie_command))
    app.add_handler(CommandHandler('romance', suggest_romance_movie_command))
    app.add_handler(CommandHandler('sciencefiction', suggest_sci_fi_movie_command))
    app.add_handler(CommandHandler('thriller', suggest_thriller_movie_command))
    app.add_handler(CommandHandler('tvmovie', suggest_tv_movie_command))
    app.add_handler(CommandHandler('war', suggest_war_movie_command))
    app.add_handler(CommandHandler('western', suggest_western_movie_command))
    app.add_handler(CommandHandler('crime', suggest_crime_movie_command))

    
    # adding handlers for messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # adding error handler
    app.add_error_handler(error)

    # running the bot through a polling technique
    print('Polling...')
    app.run_polling(poll_interval=3)