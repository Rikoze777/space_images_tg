import os


def to_list(dict):
    for item in dict:
        return item[2]


def get_img(folder):
    way = 'images/{}/'.format(folder)
    img_list = list(os.walk(way))
    return(to_list(img_list))
