import socket 

HEADER =64
PORT =  5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMART = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

cleint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cleint.connect(ADDR)
 
def send(msg):
    message = msg.encode(FORMART)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMART)  
    send_length += b' ' * (HEADER - len(send_length))
    cleint.send(send_length)
    cleint.send(message)
    print(cleint.recv(2048).decode(FORMART))
    
send("Hello world")
input()
send("Hello Tim")
input()
send("Hello john")
send(DISCONNECT_MESSAGE)