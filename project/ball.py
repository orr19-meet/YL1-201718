from turtle import Turtle, mainloop
class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx=dx
		self.dy=dy
		self.r=r
		self.shape("circle")
		self.shapesize(r/10)
		self.color(color)

	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		new_x=current_x+self.dx
		current_y=self.xcor()
		new_y=current_y+self.dy

		#qualities to check
		right_side_ball=new_x+self.r
		left_side_ball=new_x-self.r
		up_side_ball=new_y+self.r
		down_side_ball=new_x-self.r
		#above is for you to check
		
		new_dx =self.dx
		new_dy = self.dy

		self.goto(new_x,new_y)
		if (right_side_ball>=screen_width):
			new_dx= -self.dx
		if (left_side_ball<=0):
			new_dx= -self.dx
		if (up_side_ball>=screen_height):
			new_dy= -self.dy
		if (down_side_ball<=0):
			new_dy= -self.dy


#ball = Ball(50,50,5,0,80,"blue")
#ball.move(10,10)
#mainloop()
#example