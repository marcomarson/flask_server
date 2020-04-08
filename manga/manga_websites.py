import json

from utils import DecimalEncoder
from datetime import datetime
from manga.database import Database


class MangaWebsites(Database):

    def __init__(self):
        super().__init__()
        self.website_table = self.db['manga_websites']
        print("init")

    def get_website(self, name):
        """
        Method for requesting a specified manga
        :param name: Name of the manga
        :return: The manga requested
        """
        try:
            response = self.website_table.find_one({'name': name})
            return response
        except Exception as e:
            print(e)

    def insert_website(self, name, link):
        """
        Insert a new manga on the database
        :param name: Name of the Website
        :param last_episode: last episode watched
        :return:
        """
        try:
            manga_website = {
                    'name': name,
                    'link': link,
                    'structure': None,
                    'valid':True
                }

            response = self.website_table.insert_one(manga_website)
            return True
        except Exception as e:
            print(e)

    def deactivate_website(self, name):
        """
        Deactivate a website on the database
        :param name: Name of the Website
        :return:
        """
        try:
            response = self.website_table.update_one({'name': name},{ "$set": { "valid": False }})
            return response
        except Exception as e:
            print(e)



