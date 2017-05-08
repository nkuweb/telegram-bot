from pymongo import MongoClient

class MongoDB():

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client["telegram"]
        self.collection = self.db["telegramcollection"]

    def Insert(self,url,user):
        url={
            "url":url,
            "user":user
        }
        try:
            self.collection.insert(url)
            return True
        except:
            return False

    def UrlList(self):
        myresults = list(self.collection.find())
        return myresults