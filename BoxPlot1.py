data1=np.random.normal(100,10,200)
data2=np.random.normal(90,20,200)
data3=np.random.normal(80,30,200)
data=[data1,data2,data3]
fig=plt.figure(figsize=(10,7))
bp=plt.boxplot(data)
plt.show()