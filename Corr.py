df=pd.DataFrame(data=np.random.randint(0,100,size=(50,4)),columns=["A","B","C","D"])
corr=df.corr()
print(corr)