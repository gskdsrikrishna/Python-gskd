#55.Trnaspose of a matrix
# Take input for the number of rows and columns
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Initialize the matrix
matrix = []
for i in range(rows):
    row = []
    for j in range(columns):
        element = int(input("Enter the element at position ({}, {}): ".format(i, j)))
        row.append(element)
    matrix.append(row)

# Print the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Calculate the transpose of the matrix
transpose = [[matrix[j][i] for j in range(rows)] for i in range(columns)]

# Print the transpose matrix
print("Transposed Matrix:")
for row in transpose:
    print(row)