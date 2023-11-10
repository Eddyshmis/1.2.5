import threading


import client as cl
import Server as ser

client = cl.Network()
server = ser.Server_run()

thread_server = threading.Thread(target=server.start_server)
thread_server.start()

thread_client = threading.Thread(target=client.connect)
thread_client.start()

client.send_pos(str((0,0)))


print("end")