from keyboard import is_pressed
from time import sleep
from random import randint
from pyautogui import press


while(1):
    if is_pressed('home'):
        print("home pressed")
        t = randint(7,15)
        sleep(t)
        press('space')

if __name__ == __main__:
    pass
