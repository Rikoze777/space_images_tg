import requests
import os
from urllib.error import HTTPError
from urllib.request import urlretrieve
import argparse
from dotenv import load_dotenv


def apod_nasa_num(img_num, token):
    counter = 1
    nasa_url = "https://api.nasa.gov/planetary/apod"
    way = "images/apod/"
    os.makedirs(way, exist_ok=True)
    param = {
        "api_key": token,
        "count": img_num,
    }
    response = requests.get(nasa_url, params=param)
    response.raise_for_status()
    nasa_items = response.json()
    for item in nasa_items:
        url = item['url']
        extension = (''.join(url.split(".")[-1:]))
        filename = "apod_{}.{}".format(counter, extension)
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
    parser = argparse.ArgumentParser()
    parser.add_argument('amount',
                        help='Required argument')
    args = parser.parse_args()
    img_num = args.amount
    apod_nasa_num(img_num, nasa_token)


if __name__ == '__main__':
    main()
