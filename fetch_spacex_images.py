import requests
import os
from urllib.error import HTTPError
from urllib.request import urlretrieve
from help_func import create_parser


def fetch_spacex_launch(id_token):
    spacex_url = "https://api.spacexdata.com/v3/launches"
    way = "images/spacex/"
    os.makedirs(way, exist_ok=True)
    param = {
        "flight_id": id_token
    }
    response = requests.get(spacex_url, params=param)
    response.raise_for_status()
    spacex_items = response.json()
    for item in spacex_items:
        urls = item['links']['flickr_images']
        counter = 1
        for url in urls:
            filename = "spacex_{}.jpeg".format(counter)
            write_way = os.path.join(way, filename)
            try:
                urlretrieve(url, write_way)
            except FileNotFoundError:
                print("something wrong with local path")
            except HTTPError:
                print("something wrong with url")
            counter += 1


def main():
    parser = create_parser()
    id_arg = parser.parse_args()
    id_launch = id_arg.argument
    fetch_spacex_launch(id_launch)


if __name__ == '__main__':
    main()
    