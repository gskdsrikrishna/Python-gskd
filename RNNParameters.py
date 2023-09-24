import numpy as np

# Define the RNN parameters
input_size = 3  # Number of input features
hidden_size = 4  # Number of hidden units
sequence_length = 5  # Length of the input sequence

# Generate some random input data (a sequence of numbers)
input_sequence = np.random.randn(sequence_length, input_size)

# Initialize RNN weights and biases
W_xh = np.random.randn(input_size, hidden_size)  # Weight matrix for input to hidden
W_hh = np.random.randn(hidden_size, hidden_size)  # Weight matrix for hidden to hidden
b_h = np.zeros((1, hidden_size))  # Bias for hidden units

# Initialize hidden state
h_t = np.zeros((1, hidden_size))  # Initial hidden state

# Forward pass through the RNN
for t in range(sequence_length):
    x_t = input_sequence[t]  # Input at time step t
    
    # Compute the hidden state at time step t
    h_t = np.tanh(np.dot(x_t, W_xh) + np.dot(h_t, W_hh) + b_h)
    
    # You can use h_t for further processing or prediction
    
# Print the final hidden state
print("Final hidden state:")
print(h_t)