from email.policy import default
import os
import telegram
import argparse
from help_func import get_img
from dotenv import load_dotenv
import random


def main():
    load_dotenv()
    tg_token = os.environ.get("TG_TOKEN")
    bot = telegram.Bot(token=tg_token)
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', nargs='?',
                        help='Required folder path')
    folder_arg = parser.parse_args()
    path = folder_arg.folder
    if path:
        folder = "images/{}".format(path)
        bot.send_document(chat_id=-1001381382770, document=open(folder, 'rb'))
    else:
        full_pack = []
        full_pack += get_img("epic")
        full_pack += get_img("apod")
        full_pack += get_img("spacex")
        folder_img = random.choice(os.listdir("images"))
        img = random.choice([x for x in os.listdir("images/{}".format(folder_img)) 
                            if os.path.isfile(os.path.join("images/{}".format(folder_img), x))])
        img_path = f"images/{folder_img}/{img}"
        bot.send_document(chat_id=-1001381382770, document=open(img_path, 'rb'))

if __name__ == "__main__":
    main()
