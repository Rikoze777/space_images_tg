import os


def get_img(folder):
    path = 'images/{}/'.format(folder)
    img_list = os.listdir(path)
    for item in img_list:
        return item[2]
