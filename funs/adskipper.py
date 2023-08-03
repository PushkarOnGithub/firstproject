import pyautogui
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
vol = volume.GetMasterVolumeLevel()
maxvol = volume.GetVolumeRange()[0]
# pyautogui.press()
# print()
muted = volume.GetMute()

path = "D:\logosonyten3.png"
path2 = "D:\logo3.png"
path3 = "D:\logo2.png"

while True:
    a = pyautogui.locateCenterOnScreen(path, confidence=0.85)
    b = pyautogui.locateCenterOnScreen(path2, confidence=0.85)
    c = pyautogui.locateCenterOnScreen(path3, confidence=0.85)
    # print(a,b,c)
    print(time.ctime(), end="\r")
    found = (a != None or b != None or c != None)
    if (not found and not muted):
        pyautogui.press('volumemute')
        muted = True

    if (found and muted):
        pyautogui.press('volumemute')
        if vol != maxvol:
            volume.SetMasterVolumeLevel(0.0, None)
        muted = False

