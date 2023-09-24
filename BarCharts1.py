import numpy as np
import matplotlib.pyplot as plt
x=["ECE","CSE","EEE","MEC","CAI"]
girls=[10,20,30,40,50]
boys=[20,30,25,30,20]
w=0.4
bar1=np.arange(len(x))
bar2=[i+w for i in bar1]
plt.bar(bar1,girls,w,label="Girls")
plt.bar(bar2,boys,w,label="Boys")
plt.xticks(bar1+0.2,x)
plt.xlabel("Groups")
plt.ylabel("No of Students")
plt.title("Number of students in each group")
plt.legend()
plt.show()