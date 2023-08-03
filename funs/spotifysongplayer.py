import pyautogui
import time
# time.sleep(10)
try:
    x,y = pyautogui.position()
    pyautogui.moveTo(41,1050)
    pyautogui.click(button='left')
    pyautogui.typewrite("spotify")
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.click(x=59,y=187,button = 'left')
    time.sleep(1)
    pyautogui.typewrite("infinity",interval=0.2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.click(x=978,y=323,clicks=1,button='left')
    time.sleep(0.05)
    pyautogui.click(clicks=1,button='left')

    time.sleep(240)
    pyautogui.click(x=1905,y=74,clicks=1,button='left')

except KeyboardInterrupt:
    print("\n")

