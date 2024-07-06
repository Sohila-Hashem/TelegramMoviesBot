import os
from dotenv import load_dotenv
load_dotenv()
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from commands import *
from messages import *



bot_token = os.getenv("BOT_API_TOKEN")

# Error Handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'Update "{update}"\n caused error "{context.error}"')

# run app
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