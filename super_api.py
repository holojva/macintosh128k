import os
import json
import requests
import pprint
from super_hero_finder import get_data
pp = pprint.PrettyPrinter(indent=4)

directory_list = os.listdir()
if not "heroes_data.json" in directory_list :
    get_data()

API_KEY = "10218686935504422"

with open("heroes_data.json", "r+") as f :
    heroes_data = json.loads(f.read())
class NotFoundError(Exception) :
    pass
class SuperHeroAPI :
    def __init__(self, API=API_KEY, data=heroes_data) :
        self._token = API
        self._data = data
        self._url = f"https://superheroapi.com/api/{self._token}"
    def _parse_name(self, name) :
        return name.lower().title()
    def _get_id(self, name) :
        data = self._data.get(name, False)
        if data :
            return data
        else: 
            raise NotFoundError("Name not found")
    def get_hero(self, name) :
        name = self._parse_name(name)
        hero_id = self._get_id(name)
        return self._parse_api(self._url + f'/{hero_id}')
    def get_hero_stats(self, name) :
        name = self._parse_name(name)
        hero_id = self._get_id(name)
        return self._parse_api(self._url + f'/{hero_id}/powerstats')
    def _parse_api(self, url):
        response = requests.get(url, timeout=5)
        response.close()
        return response.json()
    def download_image(self, name) :
        image_url = self.get_hero_image_url(name)
        with open("hello.jpg", "wb") as f :
            response = requests.get(self.download_image("superman")["url"])
            f.write(response.content)
    def get_hero_image_url(self, name) :
        name = self._parse_name(name)
        hero_id = self._get_id(name)
        return self._parse_api(self._url + f'/{hero_id}/image')

    #TESTING

s = SuperHeroAPI()
result = s.get_hero("abe sapien")
pp.pprint(result)

