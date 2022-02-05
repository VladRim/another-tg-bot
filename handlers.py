from glob import glob
from random import choice
from telegram import ReplyKeyboardMarkup, KeyboardButton


import utils


def user_coordinates(update, context):
    context.user_data['emoji'] = utils.get_smile(context.user_data)
    coords = update.message.location
    print(coords)
    update.message.reply_text(
                             f" Ваши координаты {coords} {context.user_data['emoji']}",
                             reply_markup = utils.main_keyboard())



def send_cat_pictures(update, context):
    cat_list = glob("images/*.jp*g")
    cat_pic = choice(cat_list)
    chat_id = update.effective_chat.id

    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic, "rb"), reply_markup=utils.main_keyboard())



def talk_to_me(update, context):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
        #logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username)
    print(user_text)
    context.user_data['emoji'] = utils.get_smile(context.user_data)
    update.message.reply_text(f" {user_text} {context.user_data['emoji']}", reply_markup=utils.main_keyboard())


def greet_user(update, context):
    print("Ввызван /start")
    context.user_data['emoji'] = utils.get_smile(context.user_data)
    my_keyboard = ReplyKeyboardMarkup([["прислать котика"]])
    update.message.reply_text(f"Здравствуй {context.user_data['emoji']}",
                                reply_markup=utils.main_keyboard())
    print(context.user_data)