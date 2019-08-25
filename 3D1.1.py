

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from funcs import *
import numpy as np



#creating x,y for 3D plotting
len = 10
xx, yy = np.meshgrid(range(len), range(len))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d',aspect='equal')


#defining points
A = np.array([3,1,1])
B = np.array([1,2,3])
C = np.array([1,1,0])

#define direction vector of BC
m = C-B
print m

#defining line : x(k) = A + k*l

C1 = np.array([1,1,0]).reshape((3,1))
l1 = np.array([2,1,4]).reshape((3,1))

C2 = np.array([1,2,3]).reshape((3,1))
l2 = np.array([0,-1,-3]).reshape((3,1))

#normal of plane by cross product of l1 and l2 direction vectors
n = np.cross(([0,-1,-3]),([2,1,4]))
print n

#normal at pt B
C3 = np.array([1,2,3]).reshape((3,1))
l3 = np.array([-1,-6,2]).reshape((3,1))

#Equation of Plane is : n.T * x = c 

#defining planes
n = np.array([-1,-6,2])
c1 = -7


#corresponding z for planes
z1 = ((c1-n[0]*xx-n[1]*yy)*1.0)/(n[2])




#plotting points
ax.scatter(A[0],A[1],A[2],'o',label="Point A")
ax.scatter(B[0],B[1],B[2],'o',label="Point B")
ax.scatter(C[0],C[1],C[2],'o',label="Point C")

#generating points in Line 
l1_p = line_dir_pt(l1,C1)
l2_p = line_dir_pt(l2,C2)
l3_p = line_dir_pt(l3,C1)


#plotting planes
ax.plot_surface(xx, yy, z1, color='r',alpha=0.2)


#plotting line
plt.plot(l1_p[0,:],l1_p[1,:],l1_p[2,:],label="Line $L_1$")
plt.plot(l2_p[0,:],l2_p[1,:],l2_p[2,:],label="Line $L_2$")
plt.plot(l3_p[0,:],l3_p[1,:],l3_p[2,:],label="Line $n$")


plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()

plt.show()

	
	


##defining direction vectors of planes
#l1 = np.array([2,1,4])
#l2 = np.array([0,-1,-3])

#finding cross product
#cp = np.cross(l1,l2)
