import requests
import os
from urllib.error import HTTPError
import argparse
from dotenv import load_dotenv


def fetch_apod_images(num, token, img_path):
    nasa_url = "https://api.nasa.gov/planetary/apod"
    os.makedirs(img_path, exist_ok=True)
    params = {
        "api_key": token,
        "count": num,
    }
    response = requests.get(nasa_url, params=params)
    response.raise_for_status()
    nasa_items = response.json()
    for count, item in enumerate(nasa_items):
        apod_url = item['url']
        split_url = os.path.splitext(apod_url)
        head_url, ext = split_url
        img_response = requests.get(apod_url)
        img_response.raise_for_status()
        filename = "apod_{}{}".format(count, ext)
        file_path = os.path.join(img_path, filename)
        try:
            with open(file_path, 'wb') as img_file:
                img_file.write(img_response.content)
        except FileNotFoundError:
            print("something wrong with local path")
        except HTTPError:
            print("something wrong with url")


def main():
    load_dotenv()
    nasa_token = os.environ.get("NASA_TOKEN")
    img_path = os.environ.get("APOD_PATH")
    parser = argparse.ArgumentParser()
    parser.add_argument('amount',
                        help='Required image amount')
    args = parser.parse_args()
    img_amount = args.amount
    fetch_apod_images(img_amount, nasa_token, img_path)


if __name__ == '__main__':
    main()
