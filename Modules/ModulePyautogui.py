import pyautogui
import time

## ***FAILSAFES*** program being out of control as mouse and keyboard are in program's hand now
pyautogui.FAILSAFE = True   # When fail-safe mode is True, moving the mouse to the upper-left will raise a pyautogui.FailSafeException that can abort your program

pyautogui.PAUSE = 0.1    # Set up a 0.1 second pause after each PyAutoGUI call

## MOUSE FUNCTIONS
#XY coordinates have 0, 0 origin at top left corner of the screen. X increases going right, Y increases going down

x,y = pyautogui.position()  # current mouse x and y
print(x,y)
print(pyautogui.size())  # current screen resolution width and height

print(pyautogui.onScreen(x, y))  # True if x & y are within the screen.

pyautogui.moveTo(x+100, y+100, duration=num_seconds)  # move mouse to XY coordinates over num_second seconds
pyautogui.moveRel(x+200, y+200, duration=num_seconds)  # move mouse relative to its current position

pyautogui.dragTo(100, 200, button='left')     # drag mouse to X of 100, Y of 200 while holding down left mouse button
pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
pyautogui.drag(30, 0, 2, button='right')   # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button
#To see the real time location of the cursor
"""coordinates = [x,y]
while True:
    coordinates[0],coordinates[1] = pyautogui.position()
    print(coordinates,end = "\r")"""

pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')  #The button keyword argument can be 'left', 'middle', or 'right'

#or we can do all clicks one by one instead
"""pyautogui.rightClick(x=moveToX, y=moveToY)
pyautogui.middleClick(x=moveToX, y=moveToY)
pyautogui.doubleClick(x=moveToX, y=moveToY, interval = secs_between_clicks, button='left')
pyautogui.tripleClick(x=moveToX, y=moveToY, interval = secs_between_clicks, button='left')"""

pyautogui.mouseDown(); pyautogui.mouseUp()  # does the same thing as a left-button mouse click
pyautogui.mouseDown(button='right')  # press the right button down
pyautogui.mouseUp(button='right', x=100, y=200)  # move the mouse to 100, 200, then release the right button up.

pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)    ##Positive scrolling will scroll up, negative scrolling will scroll down
pyautogui.scroll(10)   # scroll up 10 "clicks"
pyautogui.scroll(-10)  # scroll down 10 "clicks"
pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"

##***KEYBOARD FUNCTIONS***

print(pyautogui.KEYBOARD_KEYS)
# write = typewrite
pyautogui.write('Hello world!')                 # prints out "Hello world!" instantly
pyautogui.write('Hello world!', interval=0.25)  # prints out "Hello world!" with a quarter second delay after each character
pyautogui.keyDown('shift')  # hold down the shift key
pyautogui.press('left')     # press the left arrow key
pyautogui.press('left')     # press the left arrow key
pyautogui.press('left')     # press the left arrow key
pyautogui.keyUp('shift')    # release the shift key

pyautogui.press(['left', 'left', 'left'])
pyautogui.press('left', presses=3)
with pyautogui.hold('shift'):
    pyautogui.press(['left', 'left', 'left'])
#Equivalent code of this can be
"""pyautogui.keyDown('shift')  # hold down the shift key
pyautogui.press('left')     # press the left arrow key
pyautogui.press('left')     # press the left arrow key
pyautogui.press('left')     # press the left arrow key
pyautogui.keyUp('shift')    # release the shift key"""

pyautogui.hotkey('ctrl', 'shift', 'esc')   #pressed down in order, and then released in reverse order
#Equivalent code of this can be
"""pyautogui.keyDown('ctrl')
pyautogui.keyDown('shift')
pyautogui.keyDown('esc')
pyautogui.keyUp('esc')
pyautogui.keyUp('shift')
pyautogui.keyUp('ctrl')"""

pyautogui.press('f10')

##***Message Box Functions***

a=pyautogui.alert(text='a', title='aa', button='OK')  #Displays a simple message box with text and a single OK button. Returns the text of the button clicked on.
print(a)

b=pyautogui.confirm(text='b', title='bb', buttons=['OK', 'Cancel'])  #Displays a message box with OK and Cancel buttons. Returns the text of the button clicked on.
print(b)

c=pyautogui.prompt(text='c', title='cc' , default='')    #Displays a message box with text input, and OK & Cancel buttons. Returns the text entered, or None if Cancel was clicked.
print(c)

d=pyautogui.password(text='d', title='dd', default='ddd', mask='*')  #Displays a message box with text input, and OK & Cancel buttons. Typed characters appear as *. Returns the text entered, or None if Cancel was clicked.
print(d)

##***SCREENSHOT FUNCTIONS***

im1 = pyautogui.screenshot()
im2 = pyautogui.screenshot('my_screenshot.png')
## Calling screenshot() will return an Image object (see the Pillow or PIL module documentation for details).
## Passing a string of a filename will save the screenshot to a file as well as return it as an Image object.
im = pyautogui.screenshot(region=(0,0, 300, 400))  #You can pass a four-integer tuple of the left, top, width, and height of the region to capture
pyautogui.locateOnScreen('my_screenshot.png')  #function to get the screen coordinates. The return value is a 4-integer tuple: (left, top, width, height)
pyautogui.center(4-integer tuple)
pyautogui.click('my_screenshot.png') # a shortcut version to click on the center of where the 'my_screenshot.png' was found

button7location = pyautogui.locateOnScreen('calc7key.png', confidence=0.9)
#The optional confidence keyword argument specifies the accuracy with which the function should locate the image on screen.
# This is helpful in case the function is not able to locate an image due to negligible pixel differences:

# The locateCenterOnScreen('image.png') function combines locateOnScreen('image.png') and center('image.png')

pyautogui.locateOnScreen(image, grayscale=False) - #Returns (left, top, width, height) coordinate of first found instance of the image on the screen. Raises ImageNotFoundException if not found on the screen.
pyautogui.locateCenterOnScreen(image, grayscale=False) - #Returns (x, y) coordinates of the center of the first found instance of the image on the screen. Raises ImageNotFoundException if not found on the screen.
pyautogui.locateAllOnScreen(image, grayscale=False) - #Returns a generator that yields (left, top, width, height) tuples for where the image is found on the screen.
pyautogui.locate(needleImage, haystackImage, grayscale=False) - #Returns (left, top, width, height) coordinate of first found instance of needleImage in haystackImage. Raises ImageNotFoundException if not found on the screen.
pyautogui.locateAll(needleImage, haystackImage, grayscale=False) - #Returns a generator that yields (left, top, width, height) tuples for where needleImage is found in haystackImage

###PIXEL MATCHING###
im.getpixel((100, 200))
(130, 135, 144)
pyautogui.pixelMatchesColor(100, 200, (130, 135, 144),tolerance=0)   #If you just need to verify that a single pixel matches a given pixel, call the pixelMatchesColor() function, passing it the X coordinate, Y coordinate, and RGB tuple of the color it represents


