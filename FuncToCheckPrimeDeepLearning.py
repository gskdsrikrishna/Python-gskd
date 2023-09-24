import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(np.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

# Generate a dataset of numbers and their prime/non-prime labels
def generate_dataset(num_samples=1000, max_number=10_000):
    X = np.random.randint(1, max_number, size=num_samples)
    Y = np.array([1 if is_prime(x) else 0 for x in X])
    return X, Y

# Generate the dataset
X_train, Y_train = generate_dataset()
X_test, Y_test = generate_dataset(200)

# Create a neural network model
model = keras.Sequential([
    Dense(16, activation='relu', input_shape=(1,)),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')  # Sigmoid activation for binary classification
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, Y_train, epochs=50, batch_size=32, validation_split=0.2)

# Evaluate the model on the test dataset
loss, accuracy = model.evaluate(X_test, Y_test)
print(f"Test loss: {loss:.4f}")
print(f"Test accuracy: {accuracy:.4f}")

# Example: Predict if a number is prime or not
input_example = np.array([10])  # Change this to the number you want to check
prediction = model.predict(input_example)
if prediction > 0.5:
    print(f"{input_example[0]} is predicted as PRIME.")
else:
    print(f"{input_example[0]} is predicted as NON-PRIME.")