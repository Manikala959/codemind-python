def absolute_difference_matrices(N, matrixA, matrixB):
    result = []  # Initialize an empty list for the result matrix

    for i in range(N):
        row = []  # Initialize an empty list for the current row
        for j in range(N):
            diff = abs(matrixA[i][j] - matrixB[i][j])  # Calculate the absolute difference
            row.append(diff)  # Add the difference to the current row
        result.append(row)  # Add the current row to the result matrix

    return result

# Input
N = int(input())
matrixA = []
matrixB = []

for i in range(N):
    rowA = list(map(int, input().split()))
    matrixA.append(rowA)

for i in range(N):
    rowB = list(map(int, input().split()))
    matrixB.append(rowB)

# Calculate the absolute difference
result_matrix = absolute_difference_matrices(N, matrixA, matrixB)

# Output the result
for row in result_matrix:
    print(*row)
