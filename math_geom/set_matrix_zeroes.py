# https://leetcode.com/problems/set-matrix-zeroes/description/

# TC - O(R*C), SC - O(1)
def setZeroes(matrix):
    if not matrix or not matrix[0]:
        return

    ROWS, COLS = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False

    # Check if first row has any zero
    for j in range(COLS):
        if matrix[0][j] == 0:
            first_row_zero = True
            break

    # Check if first column has any zero
    for i in range(ROWS):
        if matrix[i][0] == 0:
            first_col_zero = True
            break

    # Use first row and column as markers
    for i in range(1, ROWS):
        for j in range(1, COLS):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark first cell of row
                matrix[0][j] = 0  # Mark first cell of column

    # Set rows to zero based on first column
    for i in range(1, ROWS):
        if matrix[i][0] == 0:
            for j in range(1, COLS):
                matrix[i][j] = 0

    # Set columns to zero based on first row
    for j in range(1, COLS):
        if matrix[0][j] == 0:
            for i in range(1, ROWS):
                matrix[i][j] = 0

    # Set first row to zero if needed
    if first_row_zero:
        for j in range(COLS):
            matrix[0][j] = 0

    # Set first column to zero if needed
    if first_col_zero:
        for i in range(ROWS):
            matrix[i][0] = 0

# Test cases
def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

# Test case 1
matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
print("Test case 1 input:")
print_matrix(matrix1)
setZeroes(matrix1)
print("Test case 1 output:")
print_matrix(matrix1)

# Test case 2
matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print("Test case 2 input:")
print_matrix(matrix2)
setZeroes(matrix2)
print("Test case 2 output:")
print_matrix(matrix2)