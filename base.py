# -*- coding: utf-8 -*-
import pprint

from database import MongoDB
import check,os
from telegram.ext import Updater,CommandHandler,MessageHandler, Filters

Token = "361088304:AAHiOV1OPo9keiII_0l5MMXgpr273Zp2Wfk"
updater = Updater(token = Token)
dispatcher = updater.dispatcher
mongodb=MongoDB()

users=["utkucanbykl","vlademir92","badgeekluck"]


def start(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text="Bot çalışıyor.")

def hello(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text="Hello "+update.message.from_user.first_name)

def echo(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text="Merhaba "+update.message.from_user.first_name)
    bot.sendMessage(chat_id = update.message.chat_id, text="Kaynak atmak için /kaynak <link>")
    bot.sendMessage(chat_id = update.message.chat_id, text="Bota Hello dedirtmek için /hello")
    bot.sendMessage(chat_id = update.message.chat_id, text="Url Listesi için /UrlList")

def kaynak(bot, update):
    if(update.message.from_user.username not in users):
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Kaynak eklemenize izin yok .\n@utkucanbykl ya da @vlademir92 'e mesaj atıp eklenmenizi istiyebilirsiniz .")
        return
    msg = update.message.text
    x = str(msg ).replace("/kaynak"," ")
    k =  x.split(" ")
    a=check.url(k[2])
    if (a == True):
        if(mongodb.Insert(x, update.message.from_user.first_name)==False):
            bot.sendMessage(chat_id=update.message.chat_id, text="zaten var")
            return 0
        bot.sendMessage(chat_id=update.message.chat_id , text=update.message.from_user.first_name +
                                                              "'nin Kaynağı Databaseye kaydettim")
        readme = open('README.md', 'a')
        x = str(update.message.text).replace("/kaynak", " ")
        readme.write("{}".format(update.message.from_user.first_name+" <li>" + x + "</li>"))
        readme.close()
        os.system("git add -A")
        os.system("git commit -m '" + update.message.from_user.first_name + " Link '")
        os.system("git push")
        bot.sendMessage(chat_id=update.message.chat_id, text="Url github'a eklendi.")
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="URL HATALI")

def UrlList(bot, update):
    list=mongodb.UrlList()
    for i in range(len(list)):
        bot.sendMessage(chat_id=update.message.chat_id, text=list[i]["url"])

def Kaydol(bot, update):
    user = update.message.from_user.username
    chat_id = update.message.chat_id
    if(mongodb.Kaydol(user, chat_id)):
        bot.sendMessage(chat_id=update.message.chat_id, text="Kaydolundu")
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Hata")
    list=mongodb.UrlList()
    for i in range(len(list)):
        print(list[i]["name"])




#---------------HANDLER IS HERE--------------------

start_handler = CommandHandler('start', start)
hello_handler=CommandHandler('hello', hello)
echo_handler = MessageHandler(Filters.text, echo)
kaynak_handler=CommandHandler('kaynak', kaynak)
urllist_handler=CommandHandler('UrlList', UrlList)
kaydol_handler=CommandHandler('Kaydol', Kaydol)



#--------------------------------------------------
#----------------DISPATCHER IS HERE----------------

dispatcher.add_handler(echo_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(kaynak_handler)
dispatcher.add_handler(urllist_handler)
dispatcher.add_handler(kaydol_handler)

#--------------------------------------------------

updater.start_polling()
