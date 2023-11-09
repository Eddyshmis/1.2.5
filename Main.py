import turtle as tl
import classes
import threading
from functools import partial
from Server import Server_run
import time
import socket
window = tl.Screen()



size_multiplier = 6
width_window = 700
height_window = 700
window.setup(width=width_window,height=height_window,startx=None,starty=None)

Multiplayer_menu = False


play_solo_btn = classes.Button(size_multiplier,"square")
play_multiplayer_btn = classes.Button(size_multiplier,"square")

play_multiplayer_btn.place((play_multiplayer_btn.turtle.xcor() + (30*size_multiplier)),play_multiplayer_btn.turtle.ycor())
play_solo_btn.place((play_solo_btn.turtle.xcor() - (30*size_multiplier)),play_multiplayer_btn.turtle.ycor())

play_multiplayer_btn.lable("Multiplayer",'red',30)
play_solo_btn.lable("solo",'red',30)



def solo_play(x,y):
    window.clear()
    def right(player):
        if (player.xcor()+175) <= 262.5:
            player.goto(player.xcor()+175,0)
    def left(player):
        if (player.xcor()-175) >= -262.5:
            player.goto(player.xcor()-175,0)
    
        
    def set_up_solo(x,y):
        setup_crew = []
        offset_sides = 7
        print("play pressed")
        window.clear()
        set_up_man = tl.Turtle()
        set_up_man.seth(90)
        set_up_man.up()
        set_up_man.speed(0)
        set_up_man.pensize(10)
        set_up_man.goto(-350,0)
        set_up_man.down()
        set_up_man.goto(set_up_man.xcor(),(height_window/2))

        set_up_man.goto(((width_window/2) - offset_sides),set_up_man.ycor())
        set_up_man.goto(set_up_man.xcor(),-(height_window/2) + offset_sides)
        set_up_man.goto(-(width_window/2),set_up_man.ycor())
        set_up_man.goto(set_up_man.xcor(),(height_window/4))
        set_up_man.up()
        
        set_up_man.goto(0,0)

        for i in range(3):
            setup_crew.append(tl.Turtle())
        
        count_turtle = 0

        height_setup = (-height_window + 300)
        for turtle in setup_crew:
            turtle.up()
            turtle.pensize(10)
            turtle.color("Yellow")
            turtle.speed(10)

            count_turtle += 1
            turtle.seth(90)
            if count_turtle == 1:
                print(-width_window/2)
                turtle.goto(-width_window/4,height_setup)
                print(count_turtle,turtle.xcor())
            elif count_turtle == 2:
                turtle.goto(-width_window + (width_window),height_setup)
                print(count_turtle,turtle.xcor())
            elif count_turtle == 3:
                turtle.goto(width_window/4,height_setup)
                print(count_turtle,turtle.xcor())
        for turtle in setup_crew:
            turtle.down()
            turtle.goto(turtle.xcor(),turtle.ycor() + 1000)
        window.bgpic("world_gif.gif")
        set_up_man.goto(0,0)
        player = tl.Turtle()
        window.addshape("Swordfish_2.gif")
        player.shape("Swordfish_2.gif")
        player.seth(90)
        player.up()

        player.goto(-262.5,0)
        # player.goto(-87.5,0)
        # player.goto(87.5,0)
        # player.goto(262.5,0)
        tl.onkey(partial(right,player),"Right")
        tl.onkey(partial(left,player),"Left")


        

        
        

        

    
    start_game_solo_btn = classes.Button(size_multiplier,"square")
    start_game_solo_btn.place()
    start_game_solo_btn.lable("PLAY","red")
    start_game_solo_btn.click_on(set_up_solo)
    
def Multiplayer_play(x,y):
    Server = Server_run()
    window.clear()

    def Set_up_multiplayer(x,y):
        setup_crew = []
        column_left_start = 480
        column_right_start = 470
        offset_sides = 7
        print("play pressed")
        window.clear()
        set_up_man = tl.Turtle()
        set_up_man.seth(90)
        set_up_man.up()
        set_up_man.speed(0)
        set_up_man.pensize(10)
        set_up_man.goto(-350,0)
        set_up_man.down()
        set_up_man.goto(set_up_man.xcor(),(height_window/2))

        set_up_man.goto(((width_window/2) - offset_sides),set_up_man.ycor())
        set_up_man.goto(set_up_man.xcor(),-(height_window/2) + offset_sides)
        set_up_man.goto(-(width_window/2),set_up_man.ycor())
        set_up_man.goto(set_up_man.xcor(),(height_window/4))
        set_up_man.up()
        
        set_up_man.goto(0,0)

        for i in range(3):
            setup_crew.append(tl.Turtle())
        
        count_turtle = 0

        height_setup = (-height_window + 300)
        for turtle in setup_crew:
            turtle.up()
            turtle.pensize(10)
            turtle.color("Yellow")
            turtle.speed(10)

            count_turtle += 1
            turtle.seth(90)
            if count_turtle == 1:
                print(-width_window/2)
                turtle.goto(-width_window/4,height_setup)
                print(count_turtle,turtle.xcor())
            elif count_turtle == 2:
                turtle.goto(-width_window + (width_window),height_setup)
                print(count_turtle,turtle.xcor())
            elif count_turtle == 3:
                turtle.goto(width_window/4,height_setup)
                print(count_turtle,turtle.xcor())
        for turtle in setup_crew:
            turtle.down()
            turtle.goto(turtle.xcor(),turtle.ycor() + 1000)
        window.bgpic("world_gif.gif")
        set_up_man.goto(0,0)
        player = tl.Turtle()
        window.addshape("Swordfish_2.gif")
        player.shape("Swordfish_2.gif")

        
        

        

    thread = threading.Thread(target=Server.start_server)
    make_server_btn = classes.Button(size_multiplier,"square")
    make_server_btn.place()
    make_server_btn.lable("PLAY","red")
    make_server_btn.click_on(Set_up_multiplayer)
    print("hello")


play_solo_btn.click_on(solo_play)
play_multiplayer_btn.click_on(Multiplayer_play)



window.listen()
window.mainloop()