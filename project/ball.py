from turtle import Turtle
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx=dx
		self.dy=dy
		self.r=r
		self.shape="circle"
		self.shapesize(r/10)
		self.color(color, color)
	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		new_x=current_x+dx
		current_y=self.xcor()
		new_y=current_y+dy

		#qualities to check
		right_side_ball=new_x+r
		left_side_ball=new_x-r
		up_side_ball=new_y+r
		down_side_ball=new_x-r
		#above is for you to check
		
		new_dx =dx
		new_dy = dy

		self.goto(new_x,new_y)
		if (right_side_ball>=screen_width):
			new_dx= -dx
		if (left_side_ball<=0):
			new_dx= -dx
		if (up_side_ball>=screen_height):
			new_dy= -dy
		if (down_side_ball<=0):
			new_dy= -dy
