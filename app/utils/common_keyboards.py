# from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

def get_main_menu() -> str:
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
    
    return menu