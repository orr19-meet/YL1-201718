import turtle
import time
import random
from ball import *
import math


RUNNING= True
turtle.tracer(0)
turtle.hideturtle()
SLEEP=0.05
SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)
MY_BALL=Ball(0,0,0,0,30,"red")
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS =10
MAXIMUM_BALL_RADIUS =50
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

#move_all_balls()

def collide(ball_a , ball_b):
    if ball_a==ball_b:
        return False
    else:
        D = math.sqrt(math.pow((ball_a.xcor()-ball_b.xcor()),2) + math.pow((ball_a.ycor()-ball_b.ycor()),2))
        if (D+10)<=(ball_a.r + ball_b.r):
            return True
        else:
            return False

def check_all_balls_collision():
    for i in range (len(BALLS)):
        for j in range (len(BALLS)):
            ball_a = BALLS[i]
            ball_b = BALLS[j]
            if ball_a!= ball_b:
                collision = collide(ball_a , ball_b)
                if collision== True:
                    ball_a_radius =ball_a.r
                    ball_b_radius =ball_b.r
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

                    if ball_a_radius> ball_b_radius:
                        ball_a_radius+=1
                        ball_a.shapesize(ball_a_radius/10)

                        ball_b.r=new_radius
                        ball_b.goto(new_x,new_y)
                        ball_b.dx=new_dx
                        ball_b.dx=new_dx
                        ball_b.shapesize(new_radius/10)
                        ball_b.color(new_color)

                    else:
                        ball_b_radius+=1
                        ball_b.shapesize(ball_a_radius/10)

                        ball_a.r=new_radius
                        ball_a.goto(new_x,new_y)
                        ball_a.dx=new_dx
                        ball_a.dx=new_dx
                        ball_a.shapesize(new_radius/10)
                        ball_a.color(new_color)

def check_myball_collision():
    for i in range (len(BALLS)):
        ball_a = BALLS[i]
        collision = collide(ball_a , MY_BALL)
        if collision== True:
            ball_a_radius =ball_a.r 
            MY_BALL_radius =MY_BALL.r
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
            if ball_a_radius> MY_BALL_radius:
                return False
            else:
                MY_BALL.r+=1
                MY_BALL.shapesize(MY_BALL.r/10)

                ball_a.r=new_radius
                ball_a.goto(new_x,new_y)
                ball_a.dx=new_dx
                ball_a.dx=new_dx
                ball_a.shapesize(new_radius/10)
                ball_a.color(new_color)
    return True

def movearound(event):
    MY_BALL.goto((event.x-SCREEN_WIDTH),(SCREEN_HEIGHT-event.y))

turtle.getcanvas().bind("<Motion>", movearound)    
turtle.getscreen().listen()

while RUNNING== True:
    # if SCREEN_WIDTH!=int(turtle.getcanvas().winfo_width()/2)  :
    #     SCREEN_WIDTH=int(turtle.getcanvas().winfo_width()/2)

    # elif SCREEN_HEIGHT!=int(turtle.getcanvas().winfo_height()/2):
    #     SCREEN_HEIGHT=int(turtle.getcanvas().winfo_height()/2)  

    # else:
    move_all_balls()
    check_all_balls_collision()
    MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
    RUNNING = check_myball_collision()
    # print(RUNNING)
    turtle.getscreen().update()
    time.sleep(SLEEP) 



turtle.mainloop()

