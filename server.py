import socket
import threading


gamers = []
PORT = 2412
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
print('[STARTING] server is starting....')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print(f'[LISTENING] Sever is listening on {SERVER}')


def SENDMSG(txt, new):
    for PERSON in gamers:
        if PERSON != new:
            PERSON.send(txt.encode(FORMAT))

def handle(conn,addr):
    print(f'[NEW CONNECTION] {addr} conneted')
    while True:
        msg_length = conn.recv(2048).decode(FORMAT)
        if msg_length:
            if len(gamers)==2:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                SENDMSG(msg,conn)
            else:
                for x in gamers:
                    x.send('We just need 2 person!'.encode(FORMAT))

while True:
    conn, addr = server.accept()
    Thread = threading.Thread(target=handle,args=(conn,addr))
    Thread.start()
    gamers.append(conn)


