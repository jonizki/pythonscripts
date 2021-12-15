import socket
import time
import win32api


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1236))
s.listen(5)

while True:
    clientsocket, address = s.accept()

    
    #msg  = "Welcome to the server!"
    #msg = f'{len(msg):<{HEADERSIZE}}' + msg
    while True:
        time.sleep(1)
        x, y = win32api.GetCursorPos()
        #msg = f'{time.time()}'
        msg = f'{x},{y}'
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientsocket.send(bytes(msg, "utf-8"))