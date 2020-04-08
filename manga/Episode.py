from botocore.exceptions import ClientError
import datetime
from utils import DecimalEncoder
import json
from manga.database import Database


class Episode(Database):

    def __init__(self):
        super().__init__()
        self.episode_table = self.db['episode']
        print("init")

    def get_manga_episode(self, name):
        """
        Method for requesting a specified manga
        :param name: Name of the manga
        :return: The manga requested
        """
        try:
            response = self.episode_table.find_one({'episode_name': name})
            return response
        except Exception as e:
            print(e)

    def insert_manga_episode(self, name, episode_name, episode, links):
        """
        Insert a new manga episode on the database
        :param links: All links of the episode ( link of the image)
        :param episode: Number of Episode
        :param episode_name: Name of the episode
        :param name: Name of the manga
        :return:
        """
        try:
            episode={
                    'episode_name': episode_name,
                    'manga_name': name,
                    'episode': episode,
                    'link': links,
                    'seen': False,
                    'valid':True
                }

            response = self.episode_table.insert_one(episode)

            print(response.inserted_id)
            return True
        except Exception as e:
            print(e)
            return False

