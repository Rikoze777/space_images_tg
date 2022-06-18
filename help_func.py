import argparse
import os


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('argument', nargs='?', default=0,
                        help='Required argument')
    parser.add_argument('number', nargs='?', const=14400, 
                        help='Required number')
    return parser


def to_list(dict):
    for item in dict:
        return item[2]


def get_img(folder):
    way = 'images/{}/'.format(folder)
    img_list = list(os.walk(way))
    return(to_list(img_list))
