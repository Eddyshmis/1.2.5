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
        self.current_ship_pos = None

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.server.listen()
        self.meteorite = [0,0,0,0]
        
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        print(self.SERVER)

    def send_pos(self,conn):
        conn.send(str("").encode(self.FORMAT))



    def handle_client(self,conn,addr):
        counter = 0
        conn.setblocking(False)
        
        print(f"[NEW CONNECTION] {addr} connected.")
        connected = True
        while connected:
            
            connected_msg = conn.recv(2048).decode(self.FORMAT)
            
            # conn.send(str(self.currentId).encode(self.FORMAT))
            print(connected_msg)
            error_counter = 0
            sent = 0
            if connected_msg == "!Connected":
                print(f"[{addr}] {connected_msg}")
                start_game = True
                
                while start_game:
                    
                    # conn.send(str("").encode(self.FORMAT))
                    
                    try:
                        msg = conn.recv(2048).decode(self.FORMAT)
                    except:
                        msg = None
                    
                    try:
                        conn.send(str(f"{self.meteorite}").encode(self.FORMAT))
                        sent += 1
                        print("sent:" + str(sent))
                    except Exception as e:
                        if error_counter == 0:
                            print(e)
                            print("sent:" + str(sent))
                            error_counter += 1
                    
                    if not msg: 
                        pass
                    else:
                        self.current_ship_pos = msg

                        

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