import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
a = np.zeros(shape=(50,3))
count = 0
x1=[]
y1=[]
x2=[]
y2=[]
xl=[]
yl=[]
w = np.random.random_integers(10)
b = np.random.random_integers(10)
while (count < 50):
	x = np.random.uniform(low=-2.0, high=2.0, size=None)
	y = np.random.uniform(low=-2.0, high=2.0, size=None)
	if x - y > 0.001:
		l = -1
		x1.append(x)
		y1.append(y)

	elif y - x > 0.001:
		l = 1
		x2.append(x)
		y2.append(y)
	if abs(x - y) > 0.001:
		a[count] = [x,y,l]
		count += 1
	xl.append(x)
	yl.append(-(w*x)/b)
# print(xl)
# print(yl)

er = True
while (er):
	
	er = False
	for i in range(50):
		p = a[i][0]
		q = a[i][1]
		r = a[i][2]
		
		if np.sign(w*p+b*q) != r:
			er = True
			w+=0.0001*r*p
			b+=0.0001*r*q
	# print("hey")
	# print(er)
xh=[]
yh=[]
count = 0
while (count < 50):
	x = np.random.uniform(low=-2.0, high=2.0, size=None)
	xh.append(x)
	yh.append(-(w*x)/b)
	count +=1

#print(w,b)
pl.figure(1)
pl.plot(x1, y1, 'ro')
pl.plot(x2, y2, 'bo')
pl.plot(xl, yl, 'k')
pl.show()
pl.figure(2)
pl.plot(x1, y1, 'ro')
pl.plot(x2, y2, 'bo')
pl.plot(xh, yh, 'g')
pl.show()



#print(a[30][0],a[30][1],a[30][2])
