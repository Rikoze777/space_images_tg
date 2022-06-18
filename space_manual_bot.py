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
    default_argument = 0
    if folder != default_argument:
        way = "images/{}".format(folder)
        bot.send_document(chat_id=-1001381382770, document=open(way, 'rb'))
    else:
        full_pack = []
        full_pack += get_img("epic")
        full_pack += get_img("apod")
        full_pack += get_img("spacex")
        folder_img = random.choice(os.listdir("images"))
        img = random.choice([x for x in os.listdir("images/{}".format(folder_img)) 
                            if os.path.isfile(os.path.join("images/{}".format(folder_img), x))])
        way_two = f"images/{folder_img}/{img}"
        bot.send_document(chat_id=-1001381382770, document=open(way_two, 'rb'))

if __name__ == "__main__":
    main()
