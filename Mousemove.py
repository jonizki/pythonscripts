import win32api
import time
import random
import win32con

def mouse_replay(x):
    with open(x, "r") as f:
        for line in f:
            line = line.strip()
            if line == "leftclick":
                print("its left")
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                sleeptime = random.uniform(0.001,0.01)
                time.sleep(sleeptime)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            elif line == "rightclick":
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
                sleeptime = random.uniform(0.001,0.01)
                time.sleep(sleeptime)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)     
            else:
                x = str(line.partition(",")[0])
                y = str(line.partition(",")[2])
                print(x,y)
                sleeptime = random.uniform(0.000001, 0.000002)
                time.sleep(sleeptime)
                win32api.SetCursorPos((int(x),int(y)))
            

mouse_replay("mouse3.txt")
