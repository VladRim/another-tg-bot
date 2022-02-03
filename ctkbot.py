from glob import glob
import logging
from random import choice
from emoji import emojize
from telegram import ReplyKeyboardMarkup

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import token, USER_EMOJI
 

#logging.basicConfig(format="%(asctime)s - %(levelname)s - %(messages)s",
#                    filename="bot.log",
#                    level=logging.INFO) 


def get_smile(user_data):
    if "emoji" not in user_data:
        smile = choice(USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data["emoji"]

def greet_user(update, context):
    print("Ввызван /start")
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"Здравствуй {context.user_data['emoji']}")
    print(context.user_data)
    
    
 
def talk_to_me(update, context):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
        #logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username)
    print(user_text)
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f" {user_text} {context.user_data['emoji']}")
 
def send_cat_pictures(update, context):
    cat_list = glob("images/*.jp*g")
    cat_pic = choice(cat_list)
    context.bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, "rb"))

def main():
    ctkbot=Updater(token)

    #logging.info("Бот запускается")
    
    dp=ctkbot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("cat", send_cat_pictures))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
 
    ctkbot.start_polling()
    ctkbot.idle()
 
if __name__=="__main__":
    main()