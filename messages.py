import os
from telegram import Update
from telegram.ext import ContextTypes

bot_username = os.getenv("BOT_USERNAME")

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