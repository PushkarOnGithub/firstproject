import pyautogui
import pyperclip
import time

# def msg(name):
#     return f"Hello {name}, Please Join The Official Whatsapp Group of event Momentum. Here is the link to the group."

# def linkk(number):
#     return f"https://wa.me/+91{number}"

# path = "momentum participants2.csv"

# with open(path, 'r') as file:
#     file.readline()
#     time.sleep(5)
#     for i in range(28):
#         pyautogui.click(900, 65, button="left")
#         time.sleep(0.1)
#         name, number = file.readline().split(",")
#         name = name.split(" ")[0]
#         pyperclip.copy(linkk(number))
#         pyautogui.keyDown('ctrl')
#         pyautogui.press('v')
#         pyautogui.keyUp('ctrl')
#         pyautogui.press('enter')
#         time.sleep(3)
#         pyautogui.click(900, 990, button='left')
#         pyperclip.copy(msg(name=name))
#         pyautogui.keyDown('ctrl')
#         pyautogui.press('v')
#         pyautogui.keyUp('ctrl')
#         pyautogui.press('enter')

#         pyperclip.copy('https://chat.whatsapp.com/BdWIotyzVG0IEXh4BMhmtY')
#         pyautogui.keyDown('ctrl')
#         pyautogui.press('v')
#         pyautogui.keyUp('ctrl')
#         time.sleep(2.5)
#         pyautogui.press('enter')
#         time.sleep(0.25)

#         pyautogui.keyDown('alt')
#         pyautogui.press('tab')
#         pyautogui.keyUp('alt')
#         print("Message sent to : ", number, name)


def msg(i):
    return f"""
Hello,
I am *Chaitanya Dhanraj Magarde*, from Mechanical Engineering, part 2 contesting for student parliament 2023 and my *Ballot no. 18*.
I want to resolve the issues we faced in the previous session. I need your support to make this happen. I have experience of handling such things as a representative. Share this with your friends to extend your support.
Don’t forget ballot no. 1️⃣8️⃣.

Regards,
Chaitanya D. Magarde
Ballot no. 18
Your Representative
{i//2}"""

def linkk(number):
    number = number.replace(" ", "")
    return f"https://wa.me/{number}"

path = "mobilenumbers2.csv"

with open(path, 'r') as file:
    # file.readline()
    time.sleep(5)
    for i in range(79):
        pyautogui.click(900, 65, button="left")
        time.sleep(0.1)
        number = file.readline()
        pyperclip.copy(linkk(number))
        pyautogui.keyDown('ctrl')
        pyautogui.press('v')
        pyautogui.keyUp('ctrl')
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.click(900, 990, button='left')
        pyperclip.copy(msg(i))
        pyautogui.keyDown('ctrl')
        pyautogui.press('v')
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
        print("Message sent to : ", number)
