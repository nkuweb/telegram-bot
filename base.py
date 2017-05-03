# -*- coding: utf-8 -*-
import os

import check
from telegram.ext import Updater,CommandHandler,MessageHandler, Filters



Token="376593798:AAHMNABESGpXiFGiQ8Bg-0CnHc2EwyXD1hk"
updater = Updater(token=Token)
dispatcher = updater.dispatcher

def start(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Bot çalışıyor hacı")
def hello(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id,text="Hello"+update.message.from_user.first_name)
def echo(bot,update):
    if(check.url(update.message.text) != False):
        bot.sendMessage(chat_id=update.message.chat_id, text="Databaseye kaydettim")
    elif(update.message.text=="Hello"):
        bot.sendMessage(chat_id=update.message.chat_id, text="Sanada Hello")
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Boş Konuşma "+update.message.from_user.first_name)
def kaynak(bot,update):
    a=check.url(update.message.text)
    if (a != False):
        bot.sendMessage(chat_id=update.message.chat_id, text=update.message.from_user.first_name+"'nin Kaynağı Databaseye kaydettim")
        with open('telegram-bot/README.md', 'a') as the_file:
            the_file.write("<li>"+a+"</li>")


        os.system("git add .")
        os.system("git commit -m {} added".format(update.message.from_user.first_name+"'dan "+update.message.text))
        os.system("git push")

    else:
        bot.sendMessage(chat_id=update.message.chat_id,text="Url yanlış.")



#---------------HANDLER IS HERE--------------------

start_handler = CommandHandler('start', start)
hello_handler=CommandHandler('hello',hello)
echo_handler = MessageHandler(Filters.text, echo)
kaynak_handler=CommandHandler('kaynak',kaynak)

#--------------------------------------------------
#----------------DISPATCHER IS HERE----------------

dispatcher.add_handler(echo_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(kaynak_handler)

#--------------------------------------------------

updater.start_polling()
