import requests
import os
import argparse
from dotenv import load_dotenv


def fetch_spacex_launch(launch_id, img_path):
    spacex_url = "https://api.spacexdata.com/v3/launches"
    os.makedirs(img_path, exist_ok=True)
    params = {
        "flight_id": launch_id
    }
    response = requests.get(spacex_url, params=params)
    response.raise_for_status()
    spacex_items = response.json()
    for item in spacex_items:
        urls = item['links']['flickr_images']
        for count, url in enumerate(urls):
            split_url = os.path.splitext(url)
            head_url, ext = split_url
            filename = "spacex_{}{}".format(count, ext)
            img_response = requests.get(url)
            img_response.raise_for_status()
            file_path = os.path.join(img_path, filename)
            with open(file_path, 'wb') as img_file:
                img_file.write(img_response.content)


def main():
    load_dotenv()
    img_path = os.environ.get("SPACEX_PATH")
    parser = argparse.ArgumentParser()
    parser.add_argument('argument',
                        help='Required argument')
    args = parser.parse_args()
    launch_id = args.argument
    fetch_spacex_launch(launch_id, img_path)


if __name__ == '__main__':
    main()
