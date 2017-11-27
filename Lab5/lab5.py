from turtle import *
import turtle
import random
colormode(255)
size=10
class Square(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.shapesize(size)
		self.shape("square")
	def random_color(self):
		r = random.randint(0,256)
		g = random.randint(0,256)
		b = random.randint(0,256)
		self.color(r,g,b)

square1=Square(10)
square1.random_color()



class Rectangle(Turtle):
	def __init__(self,width, height,):
		Turtle.__init__(self)
		self.shapesize(size)
		turtle.home()
		turtle.begin_poly()
		turtle.fd(width)
		turtle.left(90)
		turtle.fd(height)
		turtle.left(90)
		turtle.fd(width)
		turtle.left(90)
		turtle.fd(height)
		turtle.end_poly()
		p= turtle.get_poly()
		register_shape("rectangle", p)
		self.shape("rectangle")
rectangle1=Rectangle(10,15)
rectangle1.goto(-300,-10)

turtle.home()
turtle.begin_poly()
turtle.fd(10)
turtle.left(60)
turtle.fd(10)
turtle.left(60)
turtle.fd(10)
turtle.left(60)
turtle.fd(10)
turtle.left(60)
turtle.fd(10)
turtle.left(60)
turtle.fd(10)
turtle.end_poly()
p= turtle.get_poly()
turtle.register_shape("hexagon", p)

class hexagon(Turtle):
	def __init__(self,size,):
		Turtle.__init__(self)
	
		self.shapesize(size)
		self.shape("hexagon")
hexagon1=hexagon(10)
hexagon1.goto(50,400)

class polygon(Turtle):
	def __init__(self,lines):
		turtle.__init__(self)
		self.lines=lines
		turtle.home()
		turtle.begin_poly()
		for i in range(lines):
			turtle.fd(10)
			turtle.left(360/lines)
		turtle.end_poly()
		p= turtle.get_poly()
		turtle.register_shape("polygon", p)
		self.shapesize(size)
		self.shape("polygon")
polygon1=polygon(5)
polygon1.goto(-300,500)
turtle.mainloop()