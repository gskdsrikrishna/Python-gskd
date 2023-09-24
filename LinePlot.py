import matplotlib.pyplot as plt
import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([1,2,3,4,5])
plt.plot(a,b,marker="*")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Line Plot")
plt.show()