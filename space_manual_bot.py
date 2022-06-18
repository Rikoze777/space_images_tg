import os
import telegram
from help_func import create_parser
from help_func import get_img
from dotenv import load_dotenv
import random


def main():
    load_dotenv()
    tg_token = os.environ.get("TG_TOKEN")
    bot = telegram.Bot(token=tg_token)
    parser = create_parser()
    id_arg = parser.parse_args()
    folder = id_arg.argument
    img_list = get_img(folder)
    img = random.choice(img_list)
    way = "images/{}/{}".format(folder, img)
    bot.send_document(chat_id=-1001381382770, document=open(way, 'rb'))


if __name__ == "__main__":
    main()
