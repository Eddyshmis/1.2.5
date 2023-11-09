import socket
import threading




class Server_run:
    def __init__(self):
        self.HEADER = 2084
        self.PORT = 5555
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.ADDR = (self.SERVER,self.PORT)
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"


        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.server.listen()
        
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        print(self.SERVER)

    


    def handle_client(self,conn,addr):
        
        print(f"[NEW CONNECTION] {addr} connected.")
        connected = True
        while connected:
            msg = conn.recv(2048).decode(self.FORMAT)
            # conn.send(str(self.currentId).encode(self.FORMAT))
            print(msg)
            if msg == "!Connected":
                print(f"[{addr}] {msg}")
                start_game = True
                conn.send(str("!clientListen").encode(self.FORMAT))
                # while start_game:

            if msg == "!eatshit":
                print("killyourself")

        conn.close()


    def start_server(self):
        print("[STARTING] server is starting...")
        
        
        while True:
            conn, addr = self.server.accept()
            print("connected to: ", addr)

            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            # self.currentId += 1
            print(f"[ACTIVE CONNECTIONS]{threading.active_count() - 1}")