import ctypes
from os.path import abspath
from time import sleep

while True:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abspath("wallpaper.png"), 0)
    sleep(50)
