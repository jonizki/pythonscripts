# Code to check if left or right mouse buttons were pressed
import win32api
import time

state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128

state_one_key = win32api.GetKeyState(0x31) # 1 button down 
state_two_key = win32api.GetKeyState(0x32) # 2 button down

state_esc_key = win32api.GetKeyState(0x1B) # Esc button down

startbutton = input("enter to start")

while True:
    
    
    a = win32api.GetKeyState(0x01)
    b = win32api.GetKeyState(0x02)
    c = win32api.GetKeyState(0x31)
    d = win32api.GetKeyState(0x32)
    e = win32api.GetKeyState(0x1B)

    #Gets x,y of cursor position
    x, y = win32api.GetCursorPos()
    
    #If 0 key is not pressed if 1 key is pressed
    leftclick = 0
    rightclick = 0
    one_key_pressed = 0
    two_key_pressed = 0
    esc_key_pressed = 0

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

    if c != state_one_key:  # Button state changed
        state_one_key = c
        if c < 0:
            one_key_pressed = 1
            print('Button 1 Pressed')
            
    if d != state_two_key:  # Button state changed
        state_two_key = d
        if d < 0:
            two_key_pressed = 1
            print('Button 2 Pressed')
            
    if e != state_esc_key:  # Button state changed
        state_esc_key = e
        if e < 0:
            esc_key_pressed = 1
            print('Esc Button Pressed')
            break

    
    time.sleep(0.001)

    #writes the values into a notepad
    with open("mouse3.txt", "a") as f:
        if leftclick == 1:
            f.write("leftclick" + "\n")
        if rightclick == 1:
            f.write("rightclick" + "\n")
        if one_key_pressed == 1:
            f.write("button1" + "\n")
        if two_key_pressed == 1:
            f.write("button2" + "\n")
        else:
            f.write(str(x) + "," + str(y) + "\n")
    #Sets the values back to not pressed
    leftclick = 0
    rightclick = 0
    one_key_pressed = 0
    two_key_pressed = 0

    
