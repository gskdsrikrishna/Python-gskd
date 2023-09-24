import numpy as np
x=np.random.randn(10)
y=np.random.randn(10)
print(x)
print(y)
c=np.corrcoef(x,y)
print(c)