from telegram import Update

def get_movie_response(movie: dict) -> None:
    return f"""
How about <b>'{movie["original_title"]}'?</b>\n
<b>Description</b>:\n{movie["overview"] or 'N/A'}\n
<b>Release Date: {movie["release_date"]}</b>\n
"""
