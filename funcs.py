# from translate import Translator
import random

from googletrans import Translator
import requests

import config
from schemas import NasaItem


def translate_to_rus(text: str):
    translator = Translator()
    result = translator.translate(text, dest='ru')
    return result.text


def is_url_image(image_url):
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    r = requests.head(image_url)
    if r.headers["content-type"] in image_formats:
        return True
    return False


def get_earth_img(date: str):
    items = requests.get(f"https://api.nasa.gov/EPIC/api/natural/date/{date}",
                         params={"api_key": f"{config.nasa_token}"})
    items = items.json()
    item = items[(random.randint(1, len(items) - 1))]
    image_src = item["image"]
    year, month, day = date.split("-")[0], date.split("-")[1], date.split("-")[2]
    img_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_src}.png?api_key={config.nasa_token} "
    return img_url


def get_items(search_text: str):
    res = requests.get("https://images-api.nasa.gov/search", params={"q": search_text,
                                                                     "media_type": "image"})
    items = res.json()["collection"]["items"]
    res = []
    for item in items[:10]:
        try:
            title = item["data"][0]["title"]
            desc = translate_to_rus(item["data"][0]["description"])
            img = item['links'][0]['href']
            if is_url_image(img):
                res.append(NasaItem(img=img, desc=desc, title=title))
            else:
                pass
        except KeyError:
            pass
    return res



def get_items(search_text: str):
    res = requests.get("https://images-api.nasa.gov/search", params={"q": search_text,
                                                                     "media_type": "image"})
    items = res.json()["collection"]["items"]
    res = []
    for item in items[:10]:
        try:
            title = item["data"][0]["title"]
            desc = item["data"][0]["description"]
            img = item['links'][0]['href']
            if is_url_image(img):
                res.append(NasaItem(img=img, desc=desc, title=title))
            else:
                pass
        except KeyError:
            pass
    return res


def get_apod():
    res = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={config.nasa_token}")
    return res.json()
