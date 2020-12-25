# Code to check if left or right mouse buttons were pressed
import win32api
import time

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

while True:
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)
    x, y = win32api.GetCursorPos()
    leftclick = 0
    rightclick = 0

    if a != state_left:  # Button state changed
        state_left = a
        if a < 0:
            leftclick = 1
            print('Left Button Pressed')

    if b != state_right:  # Button state changed
        state_right = b
        if b < 0:
            rightclick = 1
            print('Right Button Pressed')
    time.sleep(0.001)

    with open("mouse3.txt", "a") as f:
        if leftclick == 1:
            f.write(str(x) + "," + str(y) + "\n" + "leftclick" + "\n")
        if rightclick == 1:
            f.write(str(x) + "," + str(y) + "\n" + "rightclick" + "\n")
        else:
            f.write(str(x) + "," + str(y) + "\n")

    leftclick = 0
    rightclick = 0


    
