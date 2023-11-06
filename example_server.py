import socket
import threading

HEADER = 2084
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)



def handle_client(conn,addr):
    p = 0
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg = conn.recv(2048).decode(FORMAT)
        print(f"[{addr}] {msg}")
        if msg == "!Connected":
            p += 1
            conn.send(f"you are player {p}".encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()

