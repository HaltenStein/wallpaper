import ctypes
from datetime import datetime
from time import sleep
from os import walk, getcwd
from random import randint


SPI_SETDESKWALLPAPER = 20
PATH = getcwd()


def changeBG(paht_image: str):
    """Change background depending on bit size"""
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, paht_image, 3)


def select_path() -> list[str, str]:
    hour_now = datetime.now().hour
    if 6 <= hour_now <= 10:
        path_image = PATH + "\\image\\morning\\"
    elif 11 <= hour_now <= 17:
        path_image = PATH + "\\image\\day\\"
    else:
        path_image = PATH + "\\image\\night\\"
    return path_image, next(walk(path_image), (None, None, []))[2]


if __name__ == '__main__':
    while True:
        path_image, file_names = select_path()
        path_image = path_image + file_names[randint(0, len(file_names)-1)]
        changeBG(path_image)
        sleep(1800)
