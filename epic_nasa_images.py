import requests
import os
from urllib.error import HTTPError
from urllib.request import urlretrieve
from dotenv import load_dotenv
import re


def get_epic_img(token):
    counter = 1
    epic_url = "https://api.nasa.gov/EPIC/api/natural/images"
    way = "images/epic/"
    os.makedirs(way, exist_ok=True)
    param = {
        "api_key": token
    }
    response = requests.get(epic_url, params=param)
    response.raise_for_status()
    epic_items = response.json()
    for item in epic_items:
        base_url = "https://api.nasa.gov/EPIC/archive/natural"
        split_date = [int(x) for x in re.findall('(\d+)', item['date'])]
        edit_day = "{:02d}".format(split_date[1])
        edit_month = "{:02d}".format(split_date[2])
        img = item['image']
        img_time = f"{split_date[0]}/{edit_day}/{edit_month}"
        url = f"{base_url}/{img_time}/png/{img}.png?api_key={token}"
        filename = "epic_{}.jpeg".format(counter)
        write_way = os.path.join(way, filename)
        try:
            urlretrieve(url, write_way)
        except FileNotFoundError:
            print("something wrong with local path")
        except HTTPError:
            print("something wrong with url")
        counter += 1


def main():
    load_dotenv()
    nasa_token = os.environ.get("NASA_TOKEN")
    get_epic_img(nasa_token)


if __name__ == '__main__':
    main()
