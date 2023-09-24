#Matrix another program in Python
import numpy as np
x=np.matrix([[1,2],[3,4]])
y=np.matrix([[3,4],[5,6]])
print("Shape of matrix x:",x.shape)
print("Shape of matrix y:",y.shape)
mat_sum=np.add(x,y)
print("Matrix sum:",mat_sum)
print("Shape of mat_sum:",mat_sum.shape)