import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense

# Generate a dataset of input pairs and their sums
def generate_dataset(num_samples=1000):
    x = np.random.rand(num_samples, 2)  # Random input pairs
    y = np.sum(x, axis=1)  # Sum of input pairs
    return x, y

x_train, y_train = generate_dataset()
x_test, y_test = generate_dataset(200)

# Create a simple neural network model
model = keras.Sequential([
    Dense(16, activation='relu', input_shape=(2,)),
    Dense(8, activation='relu'),
    Dense(1)  # Output layer with a single neuron for the sum
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, epochs=25, batch_size=32, validation_split=0.2)

# Evaluate the model on the test dataset
loss = model.evaluate(x_test, y_test)
print(f"Test loss: {loss:.4f}")

# Make predictions
predictions = model.predict(x_test)

# Example: Predict the sum of [0.6, 0.3]
input_example = np.array([[0.6, 0.3]])
predicted_sum = model.predict(input_example)
print(f"Predicted sum for [0.6, 0.3]: {predicted_sum[0][0]:.4f}")