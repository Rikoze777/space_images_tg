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
    for root, dirs, files in os.walk("images/"):
        for file in files:
            if img:
                if file == img:
                    img_root = os.path.join(root, file)
            else:
                img_root = os.path.join(root, random.choice(files))
    with open(img_root, 'rb') as img_file:
        bot.send_document(chat_id=chat_id, document=img_file)


if __name__ == "__main__":
    main()
