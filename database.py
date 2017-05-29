import datetime
from pymongo import MongoClient

class MongoDB():

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client["telegra"]
        self.collection = self.db["telegracollection"]
        self.userdb = self.client["usertelegram"]
        self.usercollection = self.userdb["usercollection"]


    def Insert(self, url, user):
        urll={
            "url":url,
            "user":user,
            "date":datetime.datetime.now()
        }
        try:
            if(self.UrlCheck(str(url))==False):
                self.collection.insert(urll)
                return True
            else:
                return False
        except:
            print("Exepet")
            return False

    def UrlList(self):
        myresults = list(self.collection.find())
        return myresults

    def UrlCheck(self, url):

        if(self.collection.find_one({"url":url})):
            print("Var")
            return True
        else:
            print(url+"Yok")
            return False

    def Kaydol(self, user, chat_id):
        user={
            "name":user,
            "chat_id":chat_id
        }
        try:
            self.usercollection.insert(user)
            return True
        except:
            return False

    def UserList(self):

        myresult = list(self.usercollection.find())
        return myresult