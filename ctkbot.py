
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import token

import utils
import handlers
 

#logging.basicConfig(format="%(asctime)s - %(levelname)s - %(messages)s",
#                    filename="bot.log",
#                    level=logging.INFO) 

def main():
    ctkbot=Updater(token)

    #logging.info("Бот запускается")
    
    dp=ctkbot.dispatcher
    dp.add_handler(CommandHandler("start", handlers.greet_user))
    dp.add_handler(CommandHandler("cat", handlers.send_cat_pictures))
    dp.add_handler(MessageHandler(Filters.location, handlers.user_coordinates))
    dp.add_handler(MessageHandler(Filters.regex('^(прислать котика)$'), handlers.send_cat_pictures))
    dp.add_handler(MessageHandler(Filters.text, handlers.talk_to_me))
 
    ctkbot.start_polling()
    ctkbot.idle()
 
if __name__=="__main__":
    main()