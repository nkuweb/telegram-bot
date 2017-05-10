from pymongo import MongoClient

class MongoDB():

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client["telegram"]
        self.collection = self.db["telegramcollection"]

    def Insert(self,url,user):
        urll={
            "url":url,
            "user":user
        }
        try:
            if(self.UrlCheck(url)):
                self.collection.insert(urll)
                return True
            else:
                return False
        except:
            return False

    def UrlList(self):
        myresults = list(self.collection.find())
        return myresults

    def UrlCheck(self,url):
        sonuc=list(self.collection.find({"url":url}))
        if(url in sonuc):
            print("Var")
            return False
        else:
            print("Yok")
            return True
