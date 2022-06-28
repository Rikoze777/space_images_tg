import requests
import os
from urllib.error import HTTPError
from urllib.request import urlretrieve
import argparse


def fetch_spacex_launch(id_token):
    spacex_url = "https://api.spacexdata.com/v3/launches"
    path = "images/spacex/"
    os.makedirs(path, exist_ok=True)
    param = {
        "flight_id": id_token
    }
    response = requests.get(spacex_url, params=param)
    response.raise_for_status()
    spacex_items = response.json()
    for item in spacex_items:
        urls = item['links']['flickr_images']
        for count, url in enumerate(urls):
            file_ext = os.path.splitext(url)
            filename = "spacex_{}{}".format(count, file_ext[1])
            response_img = requests.get(url)
            response_img.raise_for_status()
            path_file = os.path.join(path, filename)
            with open(path_file, 'wb') as img_file:
                img_file.write(response_img.content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('argument',
                        help='Required argument')
    args = parser.parse_args()
    launch_id = args.argument
    fetch_spacex_launch(launch_id)


if __name__ == '__main__':
    main()
    
