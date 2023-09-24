import tensorflow as tf
from tensorflow.keras.layers import SimpleRNN, LSTM, GRU
from tensorflow.keras.models import Sequential

# Create a Sequential model
model = Sequential()

# Add a recurrent layer (SimpleRNN, LSTM, or GRU)
# Replace one of these lines with the recurrent layer of your choice:

# SimpleRNN layer:
model.add(SimpleRNN(units=64, activation='tanh', input_shape=(10, 32)))  # Example configuration

# LSTM layer:
# model.add(LSTM(units=64, activation='tanh', input_shape=(10, 32)))  # Example configuration

# GRU layer:
# model.add(GRU(units=64, activation='tanh', input_shape=(10, 32)))  # Example configuration

# You can adjust the 'units', 'activation', and 'input_shape' parameters as needed.

# Optionally, you can add more layers or output layers depending on your model architecture.

# Compile the model (example)
model.compile(optimizer='adam', loss='mse')  # Use an appropriate optimizer and loss function for your task

# Summary of the model architecture
model.summary()