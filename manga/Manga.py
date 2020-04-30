import datetime
import json
from pymongo import MongoClient
from manga.database import Database


class Manga(Database):

    def __init__(self):
        super().__init__()
        self.manga_table = self.db['manga']

    def get_manga(self, name):
        """
        Method for requesting a specified manga
        :param name: Name of the manga
        :return: The manga requested
        """
        try:
            response = self.manga_table.find_one({'name': name})
            return response
        except Exception as e:
            print(e)

    def insert_manga(self, name, last_episode):
        """
        Insert a new manga on the database
        :param name: Name of the manga
        :param last_episode: last episode watched
        :return:
        """
        try:
            manga = {
                'name': name,
                'last_episode': last_episode,
                'timestamp': datetime.utcnow().isoformat()
            }
            response = self.manga_table.insert_one(manga)
            return True
        except Exception as e:
            print(e)
            return False
