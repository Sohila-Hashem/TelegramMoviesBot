from telegram import Update, ReplyKeyboardMarkup, WebAppInfo, KeyboardButton
import requests
import os
import random

movies_api_key = os.getenv("MOVIES_API_KEY")

# utils
async def display_response(movie: dict, update: Update) -> None:
    await update.message.reply_html(f"""How about <b>'{movie["title"]}'?</b>""")
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
        return { "total_pages": 0, "results": [] }

    return data

def get_random_movie(category_id: int) -> list:
    # we need to make a first request to get the available number of pages
    num_of_pages = get_movies(category_id, 1)["total_pages"]

    random_page = random.randint(0, min(num_of_pages, 500)) # 500 is the maximum number of pages for the API
    
    movies_list = get_movies(category_id, random_page)["results"]

    random_movie_num = random.randint(0, len(movies_list) - 1)

    return movies_list[random_movie_num]
