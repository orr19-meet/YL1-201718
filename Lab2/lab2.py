'''a=[1,2,3,4,5]
def listfunc(list):
	print(list[0],list[-1])

print(listfunc(a))'''
b=[1,1,2.3,5,8,13,21,34,55,89]
'''for i in list(b):
	if i<5:
		print(i)'''

def listnum():
	newlist=[]
	for i in list(b):
		if i<5:
			newlist.append(i)
	print(newlist)
listnum()

c=[1,2,3,4,5,6,7,8,9,10,11,12,13]
def listnum3():
	newlist1=[]
	for i in list(b):
		for n in list(c):
			if i==n:
				newlist1.append(i)
	print(newlist1)
listnum3()
def prime(n):
	if n/n:
			newlist.append(i)
	print(newlist)
listnum()