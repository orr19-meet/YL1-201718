class animal(object):
	def __init__(self,sound,name,age,fav_color):
		self.sound = sound
		self.name = name
		self.age = age
		self.fav_color = fav_color
	def eat(self,food):
			print("Yummy!"+self.name+"is eating"+food)
	def description(self):
			print(self.name+"is"+self.age+"years old and loves the color"+fav_color)
	def make_sound(self,x):
			print(self.sound*x)

orr=animal("lala","orr",14,"light blue")
make_sound()
eat(knafe)
description()

