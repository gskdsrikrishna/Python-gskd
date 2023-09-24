import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,12,22,21,31,2,32,40])
plt.hist(x)
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Population")
plt.show()