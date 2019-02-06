import numpy as np
points = [(np.array([[4]]),np.array([[2]])),(np.array([[2]]),np.array([[4]]))]

#print(points

def F(w):
	value = 0
	for x,y in points:
		value = value + (x.dot(w)-y)**2

	return value/len(points)

def dF(w):
	value = 0
	for x,y in points:
		value = value + 2*(x.dot(w)-y)*x

	return value/len(points)

def gradientD():
	w = np.zeros(1)
	l = 0.01
	for i in range(50):
		f = F(w)
		g = dF(w)
		w = w - l * g
		print("iteration : {},w : {}, f : {}, g :{}".format(i,w,f,g))

gradientD()