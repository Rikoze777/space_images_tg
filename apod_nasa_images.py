import requests
import os
from urllib.error import HTTPError
import argparse
from dotenv import load_dotenv


def apod_nasa_num(num, token):
    nasa_url = "https://api.nasa.gov/planetary/apod"
    path = "images/apod/"
    os.makedirs(path, exist_ok=True)
    param = {
        "api_key": token,
        "count": num,
    }
    response = requests.get(nasa_url, params=param)
    response.raise_for_status()
    nasa_items = response.json()
    for count,item in enumerate(nasa_items):
        url = item['url']
        file_ext = os.path.splitext(url)
        response_img = requests.get(url)
        response_img.raise_for_status()
        filename = "apod_{}{}".format(count, file_ext[1])
        path_file = os.path.join(path, filename)
        try:
            with open(path_file, 'wb') as img_file:
                img_file.write(response_img.content)
        except FileNotFoundError:
            print("something wrong with local path")
        except HTTPError:
            print("something wrong with url")


def main():
    load_dotenv()
    nasa_token = os.environ.get("NASA_TOKEN")
    parser = argparse.ArgumentParser()
    parser.add_argument('amount',
                        help='Required argument')
    args = parser.parse_args()
    amount = args.amount
    apod_nasa_num(amount, nasa_token)


if __name__ == '__main__':
    main()
