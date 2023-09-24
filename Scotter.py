x=([2,4,6,8,10])
y=([1,3,5,7,9])
a=([12,14,16,18,20])
b=([11,13,15,17,19])
plt.scatter(x,y,c="pink",linewidths=2,marker="s",edgecolor="green")
plt.scatter(a,b,c="yellow",linewidths=2,marker="^",edgecolor="red")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()\