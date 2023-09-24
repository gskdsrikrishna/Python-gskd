import tensorflow as tf
from tensorflow.keras.layers import SimpleRNN
from tensorflow.keras.models import Sequential

# Define the input shape and the number of units in the RNN layer
input_shape = (10, 6)  # Replace with your actual input shape
units = 64  # Number of units in the RNN layer

# Create a Sequential model
model = Sequential()

# Add a SimpleRNN layer to the model
model.add(SimpleRNN(units, input_shape=input_shape))

# You can continue to add more layers to the model if needed

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

# Print the model summary to see the architecture
model.summary()