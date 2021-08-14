import struct
import ctypes
from datetime import datetime
from time import sleep
from os import walk, getcwd
from random import randint


SPI_SETDESKWALLPAPER = 20
PATH = getcwd()


def is_64bit_windows() -> bool:
    """Check if 64 bit Windows OS"""
    return struct.calcsize('P') * 8 == 64


def changeBG(paht_image: str):
    """Change background depending on bit size"""
    if is_64bit_windows():
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, paht_image, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, paht_image, 3)


def select_path() -> list[str, str]:
    hour_now = datetime.now().hour
    if 6 <= hour_now <= 10:
        path_image = PATH + "\\image\\morning\\"
    elif 11 <= hour_now <= 17:
        path_image = PATH + "\\image\\day\\"
    elif 18 <= hour_now <= 5:
        path_image = PATH + "\\image\\night\\"
    return path_image, next(walk(path_image), (None, None, []))[2]


if __name__ == '__main__':
    while True:
        path_image, filenames = select_path()
        path_image = path_image + filenames[randint(0, len(filenames)-1)]
        changeBG(path_image)
        sleep(1800)