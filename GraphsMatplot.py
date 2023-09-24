import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
plt.subplot(2,2,1)
plt.plot(x,np.sin(x),"-")
plt.subplot(2,2,2)
plt.plot(x,np.cos(x),"--")
plt.subplot(2,2,3)
plt.plot(x,np.exp(x),"--")
plt.subplot(2,2,4)
plt.plot(x,np.tan(x),"--")
plt.show()