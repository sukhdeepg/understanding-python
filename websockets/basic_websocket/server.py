import imp
import socket
import threading

PORT = 4000
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = 'disconnect'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f'{addr} connected')

    is_connected = True
    while is_connected:
        msg_length = int(conn.recv(HEADER).decode(FORMAT))
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            is_connected = False
        
        print(f'{addr} - {msg}')

    conn.close() 

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start(f'Active connections: {threading.activeCount() - 1}') # as we always have start fn running, we'll subtract one thread for this. 

print('Server is starting')
start()