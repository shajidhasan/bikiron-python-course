import ctypes
from time import sleep

while True:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "wallpaper.png" , 0)
    sleep(50)
