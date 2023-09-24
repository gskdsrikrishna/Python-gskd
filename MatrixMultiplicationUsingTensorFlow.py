import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten, Reshape

# Generate a dataset of matrix pairs and their products
def generate_dataset(num_samples=1000, matrix_shape=(2, 2)):
    X = []
    Y = []
    for _ in range(num_samples):
        A = np.random.rand(*matrix_shape)
        B = np.random.rand(*matrix_shape)
        C = np.dot(A, B)  # Matrix product
        X.append(np.hstack((A.flatten(), B.flatten())))  # Flatten and concatenate A and B
        Y.append(C.flatten())  # Flatten C
    return np.array(X), np.array(Y)

# Generate the dataset
X_train, Y_train = generate_dataset()
X_test, Y_test = generate_dataset(200)

# Create a neural network model for matrix multiplication
model = keras.Sequential([
    Dense(16, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(8, activation='relu'),
    Dense(np.prod(Y_train.shape[1:]), activation='linear'),  # Linear activation for matrix product
    Reshape(Y_train.shape[1:])  # Reshape to the original matrix shape
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, Y_train, epochs=25, batch_size=32, validation_split=0.2)

# Evaluate the model on the test dataset
loss = model.evaluate(X_test, Y_test)
print(f"Test loss: {loss:.4f}")

# Make predictions
predictions = model.predict(X_test)

# Example: Predict the product of two 2x2 matrices
matrix_A = np.array([[1, 1], [1, 1]])
matrix_B = np.array([[1, 1], [1, 1]])
input_example = np.hstack((matrix_A.flatten(), matrix_B.flatten()))
predicted_product = model.predict(np.array([input_example]))
predicted_product = predicted_product.reshape(matrix_A.shape)
print("Predicted Matrix Product:")
print(predicted_product)