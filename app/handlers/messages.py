from telegram import Update
from telegram.ext import ContextTypes
import config.config as config

# Message Handler
async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    bot_username = config.general['BOT_USERNAME']

    message_type: str = update.message.chat.type
    text: str = update.message.text

    if message_type == 'group':
        if bot_username in text:
            text = text.replace(bot_username, '').strip()
            response: str = reply_text(text)
        else:
            return
        
    else :
        response: str = reply_text(text)

    await update.message.reply_text(response)


def reply_text(text: str) -> str:
    processed_text = text.lower()

    if 'hello' in processed_text:
        return 'Hey there!'
    
    if 'bye' in processed_text:
        return 'Looking forward to see you again, Wish you a good day!'
    
    if 'how are you' in processed_text:
        return 'All good, thanks, and you?'
    
    return "I didn't get that. Can you please rephrase?"