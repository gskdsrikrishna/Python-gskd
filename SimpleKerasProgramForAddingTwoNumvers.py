#Simple keras program for adding two numbers
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
X=np.array([[1.0,2.0]])#Input data
y=np.array([[3.0]]) #Corresponding Output data
#Create a sequential model
model=Sequential()
#Add a single dense layer with one neuron
model.add(Dense(1,input_dim=2))
#Compile the model
model.compile(loss='mean_squared_error',optimizer='adam')
#Train the model
model.fit(X,y,epochs=500,batch_size=25,verbose=0)
#Make Predictions
result=model.predict(np.array([[2.0,4.0]]))
print("Predicted Sum:",result[0][0])