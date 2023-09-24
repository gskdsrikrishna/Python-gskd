#Finding Roots
import numpy as np
a=float(input("Enter the a coefficient:"))
b=float(input("Enter the b coefficient:"))
c=float(input("Enter the c coefiicient:"))
root=(b*b)-(4*a*c)
sq=np.sqrt(root)
print("Discriminant:",sq)
p=((-b)+sq)/(2*a)
n=((-b)-sq)/(2*a)
print("Positive Root:",p)
print("Negative Root:",n)