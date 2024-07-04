import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()

bot_token = os.getenv("BOT_API_TOKEN")
bot_username = os.getenv("BOT_USERNAME")

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, thanks for joining the chat. I am a ANA_T3ABT bot and can suggest good movies for you! :)")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("What can i help you with?")

async def suggest_a_movie_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("you definitely should see the 'As above so below' movie")


# Responses
def handle_response(text: str) -> str:
    processed_text = text.lower()

    if 'hello' in processed_text:
        return 'Hey there!'
    
    if 'bye' in processed_text:
        return 'Do not forget to subscribe! :)'
    
    if 'how are you' in processed_text:
        return 'I am fine, thanks and you?'
    
    return "I didn't get that. Can you please rephrase?"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # whether the sender is sending from a private or a group chat
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) from {message_type} sent: "{text}"')

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

    print(f'Bot sent: "{response}"')
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f'Update "{update}" caused error "{context.error}"')

if __name__ == '__main__':
    print('Starting bot...')

    app = ApplicationBuilder().token(bot_token).build()

    # adding handlers for commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('suggest_a_movie', suggest_a_movie_command))
    
    # adding handlers for messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # adding error handler
    app.add_error_handler(error)

    # running the bot through a polling technique
    print('Polling...')
    app.run_polling(poll_interval=3)