import win32api
import time


def main():
    capture_mouse()
    #save_mouse()

def capture_mouse():
    x, y = win32api.GetCursorPos()
    state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
    print(state_left)
    time.sleep(1)

    return x, y


def save_mouse():
    x, y = capture_mouse()
    with open("mouse3.txt", "a") as f:
        f.write(str(x) + "," + str(y) + "\n")


while True:
    main()


    
