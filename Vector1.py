#Vectors Program in Python
import numpy as np
x=[1,2,3]
y=[4,5,6]
print("Type of x:",type(x))
print("x+y:",x+y)
z=np.add(x,y)
print(z)
print("Type of z:",type(z))
mul=np.cross(x,y)
print("Cross Product of x and y:",mul)