import matplotlib.pyplot as plt
import numpy as np
price=np.asarray([2,4,6,8,10])
sales=np.asarray([34,56,78,43,67])
profit=np.asarray([10,20,30,40,50])
plt.scatter(x=price,y=sales,s=profit*10)
plt.show()