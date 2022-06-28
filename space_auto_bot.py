import os
from re import T
import telegram
import argparse
from help_func import get_img
from dotenv import load_dotenv
import time
import random


def publish(folder, img_list, num, bot, chat_id):
    while True:
        random.shuffle(img_list)
        for image in img_list:
            path = "images/{}/{}".format(folder, image)
            bot.send_document(chat_id=chat_id, document=open(path, 'rb'))
            time.sleep(3600*num)


def main():
    load_dotenv()
    chat_id = os.environ.get("CHAT_ID")
    tg_token = os.environ.get("TG_TOKEN")
    bot = telegram.Bot(token=tg_token)
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', 
                        help='Required folder')
    parser.add_argument('number', nargs='?', default=14400,
                        type=int, 
                        help='Required number')
    args = parser.parse_args()
    folder = args.folder
    num = args.number
    img_list = get_img(folder)
    publish(folder, img_list, num, bot, chat_id)


if __name__ == "__main__":
    main()
