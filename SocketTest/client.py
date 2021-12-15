import socket

HEADERSIZE = 10

#SOCK_STREAM -> Stream of data
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Client -> Connects to server
s.connect((socket.gethostname(), 1236))

while True:
    full_msg = ''
    new_msg = True
    while True:
        #Message buffer size
        msg = s.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg.decode("utf-8")

        if len(full_msg)-HEADERSIZE == msglen:
            print("Full msg received")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''