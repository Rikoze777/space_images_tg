import requests
import os
from urllib.error import HTTPError
from dotenv import load_dotenv
from datetime import datetime


def fetch_epic_images(token, img_path):
    epic_url = "https://api.nasa.gov/EPIC/api/natural/images"
    os.makedirs(img_path, exist_ok=True)
    params = {
        "api_key": token
    }
    response = requests.get(epic_url, params=params)
    response.raise_for_status()
    epic_items = response.json()
    for count, item in enumerate(epic_items):
        base_url = "https://api.nasa.gov/EPIC/archive/natural"
        date_time = datetime.fromisoformat(item['date']).strftime('%Y/%m/%d')
        split_time = date_time.split('/')
        year, month, day = split_time
        img = item['image']
        img_time = f"{year}/{month}/{day}"
        epic_url = f"{base_url}/{img_time}/png/{img}.png"
        img_response = requests.get(epic_url, params=params)
        img_response.raise_for_status()
        filename = "epic_{}.png".format(count)
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
    img_path = os.environ.get("EPIC_PATH")
    fetch_epic_images(nasa_token, img_path)


if __name__ == '__main__':
    main()
