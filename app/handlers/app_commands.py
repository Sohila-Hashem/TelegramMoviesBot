from telegram import Update
from telegram.ext import  ContextTypes
from app.services.Movies.movies_service import MovieCategoryMap

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Movies4U bot, What's your Movie choice for today 😀?")
    await update.message.reply_html(f"""
        {
            list(map(lambda category: f"/{category}\n", MovieCategoryMap.get_supported_categories()))
        }
    """)

async def menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("What's your Movie choice for today 😀?\n")
    await update.message.reply_html(f"""
        {
            list(map(lambda category: f"/{category}", MovieCategoryMap.get_supported_categories()))
        }
    """)