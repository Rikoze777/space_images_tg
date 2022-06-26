import os


def get_img(folder):
    way = 'images/{}/'.format(folder)
    img_list = list(os.walk(way))
    for item in img_list:
        return item[2]
