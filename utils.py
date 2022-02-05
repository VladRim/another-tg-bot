from random import choice
from telegram import ReplyKeyboardMarkup, KeyboardButton
from emoji import emojize

from config import USER_EMOJI


def main_keyboard():
    return ReplyKeyboardMarkup([["прислать котика", KeyboardButton('мои кординаты', request_location=True)]])



def get_smile(user_data):
    if "emoji" not in user_data:
        smile = choice(USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data["emoji"]
