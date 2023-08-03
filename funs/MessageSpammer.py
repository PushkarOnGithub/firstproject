import pyautogui
import time

try:
    message = input("Enter The Meassage:\n")
    tag=input("Is there a Tag in the Message? Type yes or no.\n").lower().startswith("y")
    number = int(input("Enter the number:\n"))
    print("Program Is Waiting for 15 Seconds.Choose correct Destination of the Messages wisely or Close the program By pressing \nCtrl+C")
    for i in range(15):
        time.sleep(1)
        print(f"Spamming Will Start In {15-i} seconds",end="\r")
    for i in range(number):
        pyautogui.typewrite((message),interval=0)
        pyautogui.press('Enter')
        if tag:
            pyautogui.press('Enter')
        # time.sleep(0.05)
except KeyboardInterrupt:
    print("You Closed The Program")

