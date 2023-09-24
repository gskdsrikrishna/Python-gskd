import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(np.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Generate a dataset of numbers and their prime status
def generate_dataset(num_samples=10000, max_number=1000):
    X = np.random.randint(2, max_number, size=num_samples)
    Y = np.array([is_prime(x) for x in X], dtype=int)
    return X, Y

# Generate the dataset
X_train, Y_train = generate_dataset()
X_test, Y_test = generate_dataset(2000)

# Create a neural network model
model = keras.Sequential([
    Dense(16, activation='relu', input_shape=(1,)),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')  # Sigmoid activation for binary classification
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, Y_train, epochs=20, batch_size=32, validation_split=0.2)

# Evaluate the model on the test dataset
loss, accuracy = model.evaluate(X_test, Y_test)
print(f"Test loss: {loss:.4f}, Test accuracy: {accuracy:.4f}")

# Example: Predict whether a number is prime or not
test_number = np.array([11])  # Change the number you want to test here
predicted_probability = model.predict(test_number)
is_prime_predicted = predicted_probability > 0.5
print(f"Predicted Probability: {predicted_probability[0][0]:.4f}")
print(f"Is Prime? {bool(is_prime_predicted[0][0])}")