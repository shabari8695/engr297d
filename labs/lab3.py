import numpy as np
points = [(np.array([[4]]),np.array([[2]])),(np.array([[2]]),np.array([[4]]))]
true_w = np.array([3])
inp = []
output = []
d = len(true_w)
points = []

for i in range(10000):
    x = np.random.randn(d)
    y = true_w.dot(x)+np.random.randn()
    points.append((x,y))
    inp.append(x)
    output.append(y)

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

def sF(w,i):
	x,y = points[i]
	value = (x.dot(w)-y)**2

	return value

def sdF(w,i):
	x,y = points[i]
	value = 2*(x.dot(w)-y)*x

	return value

def gradientD():
	w = np.zeros(1)
	l = 0.01
	for i in range(50):
		f = F(w)
		g = dF(w)
		w = w - l * g
		print("iteration : {},w : {}, f : {}, g :{}".format(i,w,f,g))

def stochasticGradientD():
	w = np.zeros(1)
	l = 0.01
	for i in range(50):
		for j in range(len(points)):
			f = sF(w,j)
			g = sdF(w,j)
			w = w - l * g
		
		print("iteration : {},w : {}, f : {}, g :{}".format(i,w,f,g))

stochasticGradientD()