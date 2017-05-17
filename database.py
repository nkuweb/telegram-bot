from pymongo import MongoClient

class MongoDB():

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client["telegram"]
        self.collection = self.db["telegramcollection"]

    def Insert(self,url,user):
        urll={
            "url":url,
            "user":user
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

    def UrlCheck(self,url):

        if(url in self.collection.find({"url":url})):
            print("Var")
            return True
        else:
            print(url+"Yok")
            return False
