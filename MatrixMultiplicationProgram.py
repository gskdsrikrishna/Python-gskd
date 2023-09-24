#56.Matrix Multiplication program
# Take input for the dimensions of the first matrix
rows1 = int(input("Enter the number of rows for the first matrix: "))
columns1 = int(input("Enter the number of columns for the first matrix: "))

# Initialize the first matrix
matrix1 = []
for i in range(rows1):
    row = []
    for j in range(columns1):
        element = int(input("Enter the element at position ({}, {}): ".format(i, j)))
        row.append(element)
    matrix1.append(row)

# Take input for the dimensions of the second matrix
rows2 = int(input("Enter the number of rows for the second matrix: "))
columns2 = int(input("Enter the number of columns for the second matrix: "))

# Initialize the second matrix
matrix2 = []
for i in range(rows2):
    row = []
    for j in range(columns2):
        element = int(input("Enter the element at position ({}, {}): ".format(i, j)))
        row.append(element)
    matrix2.append(row)

# Check if matrix multiplication is possible
if columns1 != rows2:
    print("Invalid matrices. Number of columns in the first matrix should be equal to the number of rows in the second matrix.")
else:
    # Perform matrix multiplication
    result = [[0 for _ in range(columns2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(columns2):
            for k in range(columns1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    # Print the result matrix
    print("Result Matrix:")
    for row in result:
        print(row)