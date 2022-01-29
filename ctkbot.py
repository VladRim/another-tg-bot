import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import token
 

logging.basicConfig(filename="bot.log", level=logging.INFO) 


def greet_user(update, context):
    print("Ввызван /start")
    update.message.reply_text("Здравствуй")
    #print(update.message)
    #update.message.reply_text(text)
 
def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)
 
def main():
    ctkbot=Updater(token,use_context=True)
    
    dp=ctkbot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
 
    ctkbot.start_polling()
    ctkbot.idle()
 
if __name__=="__main__":
    main()