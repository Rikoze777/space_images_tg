import requests
import os
from urllib.error import HTTPError
from dotenv import load_dotenv
from datetime import datetime


def get_epic_img(token):
    epic_url = "https://api.nasa.gov/EPIC/api/natural/images"
    path = "images/epic/"
    os.makedirs(path, exist_ok=True)
    param = {
        "api_key": token
    }
    response = requests.get(epic_url, params=param)
    response.raise_for_status()
    epic_items = response.json()
    for count,item in enumerate(epic_items):
        base_url = "https://api.nasa.gov/EPIC/archive/natural"
        date_time = datetime.fromisoformat(item['date']).strftime('%Y/%m/%d')
        date_time = date_time.split('/')
        img = item['image']
        img_time = f"{date_time[0]}/{date_time[1]}/{date_time[2]}"
        url = f"{base_url}/{img_time}/png/{img}.png?api_key={token}"
        response_img = requests.get(url)
        response_img.raise_for_status()
        filename = "epic_{}.png".format(count)
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
    get_epic_img(nasa_token)


if __name__ == '__main__':
    main()
