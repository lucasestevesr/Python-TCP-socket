import socket
import threading

header = 64
server_name = socket.gethostbyname(socket.gethostname())
port = 7777
address = (server_name, port)
disconnect_msg = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)


def handle_client(conn, addr):
    print(f"New Connection {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(header).decode('utf-8')
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode('utf-8')
            if msg == disconnect_msg:
                connected = False

            print(f"{addr} - {msg}")
            conn.send("Msg received.".encode('utf-8'))

    conn.close()

def start():
    server.listen()
    print(f"Server running on {server_name}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active connections {threading.activeCount()-1}")

print("Server is starting...")
start()