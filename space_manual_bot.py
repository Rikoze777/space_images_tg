import os
import telegram
import argparse
from dotenv import load_dotenv
import random


def main():
    load_dotenv()
    chat_id = os.environ.get('CHAT_ID')
    tg_token = os.environ.get("TG_TOKEN")
    bot = telegram.Bot(token=tg_token)
    parser = argparse.ArgumentParser()
    parser.add_argument('image', nargs='?',
                        help='Required folder path')
    folder_arg = parser.parse_args()
    img = folder_arg.image
    if img:
        for root, dirs, files in os.walk("images/"):
            for file in files:
                if file==img:
                    img_root = os.path.join(root, file)
        bot.send_document(chat_id=chat_id, document=open(img_root, 'rb'))
    else:
        img_list = []
        for root, dirs, files in os.walk("images/"):
            for file in files:
                img_root = os.path.join(root, file)
                img_list.append(img_root)
        img_path = random.choice(img_list)
        bot.send_document(chat_id=chat_id, document=open(img_path, 'rb'))


if __name__ == "__main__":
    main()
