import turtle as tl
import time
import socket
class Button():
    def __init__(self,size_multiplier,shape,color = "black"):
        self.size_multiplier = size_multiplier
        self.shape = shape
        self.turtle = tl.Turtle()

        tl.tracer(0,0)

        self.turtle.speed(0)
        self.turtle.color(color)
        self.turtle.shapesize((1 * size_multiplier),(1 * size_multiplier))
        self.turtle.up()
        self.turtle.shape(f"{shape}")
        self.turtle.hideturtle()
        tl.tracer(1,0)
    def place(self,x:float = 0,y:float = 0):
        tl.tracer(0,0)
        self.x = x
        self.y = y
        self.turtle.hideturtle()
        self.turtle.goto(x,y)
        self.turtle.showturtle()
        tl.tracer(1,0)
    def click_on(self,func):
        '''add x,y parameters for the inputed function
        \ndef print_test(x,y):
            print("works")'''
        self.turtle.onclick(func)
    def click_off(self):
        self.turtle.onclick(None)
    def lable(self,text,color,size = 30):
        self.turtle.goto(self.turtle.xcor(),(self.turtle.ycor() + (10*self.size_multiplier)))
        self.turtle.pencolor(color)
        self.turtle.write(f"{text}",False,"center",("Arial",size,"normal"))
        self.turtle.goto(self.turtle.xcor(),(self.turtle.ycor() - (10*self.size_multiplier)))
# test_turt = Button(2.5,"square")
# test_turt.place(100,10)


# tl.mainloop()