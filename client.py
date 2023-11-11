import socket
# import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostbyname(socket.gethostname()) 
        self.port = 5555
        self.FORMAT = 'utf-8'
        self.addr = (self.server, self.port)
        self.sent = 0
        self.server_msg = None
        self.counter = 0
        
        




    def send(self, data):
        try:
            self.client.send(str.encode(data))
            # # return pickle.loads(self.client.recv(2048*2))
            # return self.client.recv(2048)
        except socket.error as e:
            print(e)
    def receive_data(self):
        try:
            return self.client.recv(12).decode(self.FORMAT)
        except:
            return None


    def send_and_receive(self,pos):
        '''sends the pos of ship and sets server_msg as the received data'''
        self.send(str(pos))
        # must set setblocking as False or it will wait for message
        self.server_msg = self.receive_data()
    
    def connect(self):
        self.client.connect(self.addr)
        self.client.setblocking(False)
        print("Player connected to: ",self.addr)
        self.send("!Connected")
        # Server_msg = self.client.recv(2048).decode(self.FORMAT)
        

        
    def get_pos(self):
        self.send('!GetPOS')
        Server_msg_pos = self.client.recv(2048).decode(self.FORMAT)
        print(Server_msg_pos,"Network end",type(Server_msg_pos))
        return Server_msg_pos
    def send_pos_ready(self,pos):
        self.send(str(pos))

    def test_messages(self):
        self.send('!eatshit')
    
    def send_pos(self,cords):
        print(type(cords) )
        print("count: ",len(cords),cords )
        if int(len(cords)) < 12:
            diff = int(len(cords)) - 13
            cords = cords + (" " * diff)
        else:
            self.send(cords)
            self.player_2_pos = self.client.recv(12).decode(self.FORMAT)
            print(self.player_2_pos)
    


# test_network = Network()
# print(test_network.connect())
# test_network.test_messages()