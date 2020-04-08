from pymongo import MongoClient
import configparser

class Database(object):

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('db.ini')
        self.client = MongoClient(config['mongo']['access'])
        self.db = self.client.dev

