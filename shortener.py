# from database import Database, insert, get_url
# import string
# import random

# class Shortener:
#     def __init__(self):
#         self.db = Database()

#     def shorten(self, url):
#         short_url = self.generate_short_url(url)
#         self.db.insert(url, short_url)
#         return short_url

#     def generate_short_url(self, url):
#         characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
#         return ''.join(random.choices(characters, k = 7))

#     def get_url(self, short_url):
#         return self.db.get_url(short_url)
from database import Database
import string
import random

class Shortener:
    def __init__(self):
        self.db = Database()

    def shorten(self, url):
        short_url = self.generate_short_url()
        self.db.insert(url, short_url)
        return short_url

    def generate_short_url(self):
        characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choices(characters, k=7))

    def get_url(self, short_url):
        return self.db.get_url(short_url)
