import numpy as np

# Define the RNN architecture
input_size = 3  # Number of input features
hidden_size = 4  # Number of hidden units
output_size = 2  # Number of output units

# Initialize weights and biases
Wxh = np.random.randn(hidden_size, input_size)  # Input to hidden weights
Whh = np.random.randn(hidden_size, hidden_size)  # Hidden to hidden weights
Why = np.random.randn(output_size, hidden_size)  # Hidden to output weights
bh = np.zeros((hidden_size, 1))  # Hidden bias
by = np.zeros((output_size, 1))  # Output bias

# Define the forward pass through the RNN
def forward_pass(inputs):
    xs, hs, ys, ps = {}, {}, {}, {}
    
    hs[-1] = np.zeros((hidden_size, 1))  # Initial hidden state
    
    # Forward pass
    for t in range(len(inputs)):
        xs[t] = inputs[t]
        hs[t] = np.tanh(np.dot(Wxh, xs[t]) + np.dot(Whh, hs[t-1]) + bh)
        ys[t] = np.dot(Why, hs[t]) + by
        ps[t] = np.exp(ys[t]) / np.sum(np.exp(ys[t]))  # Softmax for probabilities
    
    return xs, hs, ys, ps

# Test the RNN with some example inputs
inputs = [np.array([[1], [0], [0]]), np.array([[0], [1], [0]]), np.array([[0], [0], [1]])]

xs, hs, ys, ps = forward_pass(inputs)

# Print the final probabilities for each input
for t in range(len(inputs)):
    print(f"Input {t+1}:")
    print(f"Probability Distribution: {ps[t]}")