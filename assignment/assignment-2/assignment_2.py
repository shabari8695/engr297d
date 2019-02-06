import numpy as np
import random
import math
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False 


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

#copy the code from lab2 for F(),dF() and gradientDescent()
#run the gradientDescent function for the new set of points provided.
#compare the value of the valiable 'w' in the gradientDescent function with value of variable true_w