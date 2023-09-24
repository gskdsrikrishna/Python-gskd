import pandas as pd
data={"Name":["Gskd","Bhumi","vijay"],"Age":[19,17,15],"Class":[14,12,9]}
df=pd.DataFrame(data)
print(df[["Name","Class"]])
print(gskd.head())
print(gskd.tail())
print(gskd.describe())
print(gskd.iloc[0:3,0:2])
a=gskd.drop("Class",axis=1)
print(a)
b=gskd.drop([1,2,3],axis=0)
print(b)
print(gskd.mean())
print(gskd.min())
import matplotlib.pyplot as plt
plt.hist(gskd["Class"],bins=30,color="red")
plt.show()
print(gskd.shape)
list(gskd["Age"].value_counts()[0:3].keys())
gskd["Age"].value_counts()[0:3]
plt.hist(gskd["Class"])
plt.show()
