import pymongo 
import urllib 
from flask_pymongo import PyMongo
from settings import MONGO_DATABASE

class MonogoDatabase:
    def __init__(self) :
        self.host = MONGO_DATABASE["HOST"] 
        self.user_name = MONGO_DATABASE["USER_NAME"]
        self.password = MONGO_DATABASE["PASSWORD"]
        self.port = MONGO_DATABASE["PORT"]
        self.mongo_uri = self.host + self.user_name + urllib.parse.quote(self.password) + self.port
        self.client = None

    def _init_db(self) :
        self.client = pymongo.MongoClient(self.mongo_uri) 
        return self.client.youtube_data
    