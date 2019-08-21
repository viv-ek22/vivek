#This program draws a hyperbola
import numpy as np
import matplotlib.pyplot as plt
import math
from coeffs import *

# for plotting hyperbola
x = np.linspace(-15,15,50)
y1 = np.sqrt((3*(x**2)-72)/4)
y2 = -np.sqrt((3*(x**2)-72)/4)

# for generating line AB
A = np.array([13.56,0]) 
B = np.array([0,12.12]) 

AB= line_gen(A,B)
plt.plot(AB[0,:],AB[1,:])

#FOR point P (point of intesction)
m1= np.array([.894,1])
n1= np.array([2.682,-4])
coeff1 =np.vstack((m1,n1))
b1= np.array([12.12,0])
P= np.linalg.solve(coeff1,b1)
print (P)
plt.text(P[0],P[1],'P')

plt.plot(x,y1,x,y2)
plt.grid()


plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.001), A[1] * (1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.001), B[1] * (1) , 'B')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axis('equal')
plt.savefig('./figs/q33_hyperbola.eps')
plt.show()
