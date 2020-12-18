import win32api
import time

def mouse_replay(x):
    with open(x, "r") as f:
        for line in f:
            x = int(line.partition(",")[0])
            y = int(line.partition(",")[2])
            time.sleep(0.1)
            win32api.SetCursorPos((x,y))

mouse_replay("mouse3.txt")
