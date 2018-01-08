import turtle
import time
import random
from ball import *

turtle.tracer(0)
turtle.hideturtle()
RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2
MY_BALL=Ball(0,0,0,2,100,"red")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS =10
MAXIMUM_BALL_RADIUS =100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
BALLS =[]
#for i in range()

turtle.mainloop()

