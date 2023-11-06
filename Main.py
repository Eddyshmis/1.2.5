import turtle as tl
import classes
from Server import Server_run
import time
import socket
window = tl.Screen()
player = tl.Turtle()


size_multiplier = 6
width_window,height_window = window.screensize()



play_solo_btn = classes.Button(size_multiplier,"square")
play_multiplayer_btn = classes.Button(size_multiplier,"square")

play_multiplayer_btn.place((play_multiplayer_btn.turtle.xcor() + (30*size_multiplier)),play_multiplayer_btn.turtle.ycor())
play_solo_btn.place((play_solo_btn.turtle.xcor() - (30*size_multiplier)),play_multiplayer_btn.turtle.ycor())

play_multiplayer_btn.lable("Multiplayer",'red',30)
play_solo_btn.lable("solo",'red',30)

def solo_play(x,y):
    window.clear()
def Multiplayer_play(x,y):
    Server = Server_run()
    Server.start_server()
    window.clear()


play_solo_btn.click_on(solo_play)
play_multiplayer_btn.click_on(Multiplayer_play)




window.mainloop()