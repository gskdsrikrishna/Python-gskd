import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,10)
print(x)
y1=x
print(y1)
y2=x**2
print(y2)
y3=x**3
print(y3)
y4=np.sqrt(x)
print(y4)
plt.subplot(2,2,1)
plt.plot(x,y1,"g--")
plt.title("y=x")
plt.subplot(2,2,2)
plt.plot(x,y2)
plt.title("y=x**2")
plt.subplot(2,2,3)
plt.plot(x,y1,"r*")
plt.title("y=x**3")
plt.subplot(2,2,4)
plt.plot(x,y1,"go")
plt.title("y=x**0.5")
plt.show()