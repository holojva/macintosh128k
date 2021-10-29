import json
import requests
from bs4 import BeautifulSoup

URL = "https://www.superheroapi.com/ids.html"
from typing import cast
import requests
from bs4 import BeautifulSoup
# url = f"https://kidkodschool.github.io/welcome"
import sys
import random
import time
# response = requests.get(url)
print(sys.argv)
# query = sys.argv[1] if len(sys.argv) > 1 else input("ima avatara ")
# print(query)
# print(dir(response))
# print(response.status_code)
# print(response.headers)
# with open("./python_is_cool.html", "wb") as f :
#     f.write(response.content)
# query = "cats"

def get_data() :
    url = f"https://superheroapi.com/ids.html"
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    count = 0
    randnum = random.randint(1, 20)
    dictio = dict()
    for raw_img in soup.find_all("td"):
        # print("Searching...")
        # You can delete this if you don't want to wait
        # time.sleep(1)
        # link = raw_img.get()
        print(raw_img)
        an_string = str(raw_img)
        an_string = an_string[4:len(an_string)-5]
        count += 1
        if count % 2 == 1 :
            hello = an_string
        else :
            dictio[an_string] = hello
        with open("heroes_data.json", "w+") as f:
            jsondata = json.dumps(dictio)
            f.write(jsondata)
    print(dictio)
# alternative = raw_img.get("alt")
# if link and link.startswith("https") and alternative != "Google":
#     count += 1
#     if randnum == count :
#         response = requests.get(link)
#         with open(f"./today_avatar.jpg", "wb") as f :
#             f.write(response.content)
#             print("Found!")
#              
#             break