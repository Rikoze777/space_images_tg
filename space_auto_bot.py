import os
import telegram
from help_func import create_parser
from help_func import get_img
from dotenv import load_dotenv
import time
import random


def publish(num, img_list, folder, bot):
    while True:
        random.shuffle(img_list)
        for item in img_list:
            way = "images/{}/{}".format(folder, item)
            bot.send_document(chat_id=-1001381382770, document=open(way, 'rb'))
            time.sleep(3600*num)


def main():
    load_dotenv()
    tg_token = os.environ.get("TG_TOKEN")
    bot = telegram.Bot(token=tg_token)
    parser = create_parser()
    id_arg = parser.parse_args()
    num = id_arg.number
    folder = id_arg.argument
    img_list = get_img(folder)
    publish(num, img_list, folder, bot)


if __name__ == "__main__":
    main()
