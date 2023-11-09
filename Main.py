import turtle as tl
import classes
import threading
from functools import partial
from Server import Server_run
import time
window = tl.Screen()



size_multiplier = 6
width_window = 700
height_window = 700
window.setup(width=width_window,height=height_window,startx=None,starty=None)

Multiplayer_menu = False


play_solo_btn = classes.Button(size_multiplier,"square")
play_multiplayer_btn = classes.Button(size_multiplier,"square")
Connect_play_btn = classes.Button(size_multiplier,"square")

play_multiplayer_btn.place((play_multiplayer_btn.turtle.xcor() + (30*size_multiplier)),play_multiplayer_btn.turtle.ycor())
play_solo_btn.place((play_solo_btn.turtle.xcor() - (30*size_multiplier)),play_multiplayer_btn.turtle.ycor())
Connect_play_btn.place(y=-200)

play_multiplayer_btn.lable("Multiplayer",'red',30)
play_solo_btn.lable("solo",'red',30)
Connect_play_btn.lable("connect play","red",size=25)


def solo_play(x,y):
    window.clear()
    def check_pos_ship(player):
        ship_pos = 0
        if player.xcor() >= -350 and player.xcor() <= -175:
            ship_pos = 1
            print("ship pos:" + str(ship_pos))
        elif player.xcor() >= -175 and player.xcor() <= 0:
            ship_pos = 2
            print("ship pos:" + str(ship_pos))
        elif player.xcor() >= 0 and player.xcor() <= 175:
            ship_pos = 3
            print("ship pos:" + str(ship_pos))
        elif player.xcor() >= 175 and player.xcor() <= 350:
            ship_pos = 4
            print("ship pos:" + str(ship_pos))
    def right(player):

        if (player.xcor()+175) <= 262.5:
            tl.onkey(None,"Right")
            player.goto(player.xcor()+175,0)
            tl.onkey(partial(right,player),"Right")
            check_pos_ship(player)

    def left(player):

        if (player.xcor()-175) >= -262.5:
            tl.onkey(None,"Left")
            player.goto(player.xcor()-175,0)
            tl.onkey(partial(left,player),"Left")
            check_pos_ship(player)

    
        
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
        
        set_up_man.hideturtle()

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
    def check_pos_ship(player):
        ship_pos = 0
        if player.xcor() >= -350 and player.xcor() <= -175:
            ship_pos = 1
            print("ship pos:" + str(ship_pos))
        elif player.xcor() >= -175 and player.xcor() <= 0:
            ship_pos = 2
            print("ship pos:" + str(ship_pos))
        elif player.xcor() >= 0 and player.xcor() <= 175:
            ship_pos = 3
            print("ship pos:" + str(ship_pos))
        elif player.xcor() >= 175 and player.xcor() <= 350:
            ship_pos = 4
            print("ship pos:" + str(ship_pos))
    def right(player):

        if (player.xcor()+175) <= 262.5:
            tl.onkey(None,"Right")
            player.goto(player.xcor()+175,0)
            tl.onkey(partial(right,player),"Right")
            check_pos_ship(player)

    def left(player):

        if (player.xcor()-175) >= -262.5:
            tl.onkey(None,"Left")
            player.goto(player.xcor()-175,0)
            tl.onkey(partial(left,player),"Left")
            check_pos_ship(player)
    

    def Set_up_multiplayer(x,y):
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
        
        set_up_man.hideturtle()

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

        
        

        

    thread = threading.Thread(target=Server.start_server)
    thread.start()
    make_server_btn = classes.Button(size_multiplier,"square")
    make_server_btn.place()
    make_server_btn.lable("PLAY","red")
    make_server_btn.click_on(Set_up_multiplayer)

def connect_play(x,y):
    window.clear()
    import client

    def get_msg():
        cl = client.Network()
        msg = cl.connect()
        return get_msg
    def check_pos_ship_lan():
        iteration_counter = 0
        ship_pos = 0
        if iteration_counter == 0:
            
            thread = threading.Thread(target=get_msg())
            thread.start()
            iteration_counter += 1
        if msg == "!clientListen":
            print("works")
        

    
        
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
        
        set_up_man.hideturtle()

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
        tl.ontimer(check_pos_ship_lan,1)
        

        

        
        

        

    
    connect_play_start_btn = classes.Button(size_multiplier,"square")
    connect_play_start_btn.place()
    connect_play_start_btn.lable("PLAY","red")
    connect_play_start_btn.click_on(set_up_solo)


play_solo_btn.click_on(solo_play)
play_multiplayer_btn.click_on(Multiplayer_play)
Connect_play_btn.click_on(connect_play)



window.listen()
window.mainloop()