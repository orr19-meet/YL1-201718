from turtle import *
import random
import math
import turtle

class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)

ball1=Ball(5,"blue",50)
ball2=Ball(4,"green",40)
##ball1.left(25)
##ball1.forward(100)

def check_collision(ball1,ball2):
	if (math.sqrt(math.pow(ball1.xcor()-ball2.xcor(),2)+math.pow(ball1.ycor()-ball2.ycor(),2)))<=(ball1.shapesize()[0]+ball2.shapesize()[0]):
		ball1.color("red")
		ball2.color("yellow")
		ball2.speed(100)

check_collision(ball1,ball2)
turtle.mainloop()