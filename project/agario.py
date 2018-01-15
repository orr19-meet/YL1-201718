import turtle
import time
import random
from ball import *
import math

#turtle.tracer(0)
turtle.hideturtle()
RUNNING=True
SLEEP=0.0077
SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)
MY_BALL=Ball(0,0,0,2,100,"red")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS =10
MAXIMUM_BALL_RADIUS =100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5
colors=['red','blue',"green",'yellow','brown','pink','purple','orange']
BALLS =[]
for i in range(NUMBER_OF_BALLS):
    new_x=random.randint((-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS),(SCREEN_WIDTH-MAXIMUM_BALL_RADIUS))
    new_y=random.randint(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS , (SCREEN_HEIGHT-MAXIMUM_BALL_RADIUS))
    new_dx=random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
    while new_dx==0:
        new_dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)

    new_dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
    while new_dy==0:
        new_dy=random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
    new_radius=random.randint( MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
    
    new_color = random.choice(colors)
    new_ball=Ball(new_x,new_y,new_dx,new_dy,new_radius,new_color)
    BALLS.append(new_ball)

def  move_all_balls():
    for i in BALLS:
        i.move(SCREEN_WIDTH,SCREEN_HEIGHT)

move_all_balls()

def collide(ball_a , ball_b):
    if ball_a==ball_b:
        return False
    else:
        D = math.sqrt(math.pow((ball_a.xcor()-ball_b.xcor()),2) + math.pow((ball_a.ycor()-ball_b.ycor()),2))



turtle.mainloop()

