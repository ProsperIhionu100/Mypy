import socket 
import threading

HEADER =64
PORT =  5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMART = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handleclient(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMART) 
        if msg_length:
            msg_length =int(msg_length)
            msg = conn.recv(msg_length).decode(FORMART)
            if msg == DISCONNECT_MESSAGE:
                    connected = False
            print(f"[{addr}] {msg}")
            conn.send("msg received".encode(FORMART))
    conn.close()
        
def start():
    server.listen()
    print(f"[LISTENING] Serrver is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handleclient, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        

print("[STARTING] server is starting....")
start()
