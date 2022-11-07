import socket

header = 64
server_name = socket.gethostbyname(socket.gethostname())
port = 7777
address = (server_name, port)
disconnect_msg = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

def send(msg):
    message = msg.encode('utf-8')
    msg_length = len(message)
    send_length = str(msg_length).encode('utf-8')
    send_length += b' ' * (header - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(1024).decode('utf-8'))

send("Hello World!")
send("Hello Alex!")
send("What about the blockchain project?")

send(disconnect_msg)