# https://leetcode.com/problems/spiral-matrix

# TC - O(R*C), SC - O(1)
def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []

    ROWS, COLS = len(matrix), len(matrix[0])
    result = []
    TOP, BOT = 0, ROWS - 1
    L, R = 0, COLS - 1

    while TOP <= BOT and L <= R:
        # Traverse Right
        for j in range(L, R + 1):
            result.append(matrix[TOP][j])
        TOP += 1

        # Traverse down
        if TOP <= BOT:
            for i in range(TOP, BOT + 1):
                result.append(matrix[i][R])
            R -= 1

        # Traverse Left
        if TOP <= BOT and L <= R:
            for j in range(R, L - 1, -1):
                result.append(matrix[BOT][j])
            BOT -= 1

        # Traverse up
        if TOP <= BOT and L <= R:
            for i in range(BOT, TOP - 1, -1):
                result.append(matrix[i][L])
            L += 1

    return result

# Test case 1
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(spiralOrder(matrix1))  # Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]

# Test case 2
matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(spiralOrder(matrix2))  # Expected: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

matrix3 = [[1]]  # Single element
print(spiralOrder(matrix3))  # Expected: [1]

matrix4 = [[1, 2], [3, 4]]  # 2x2 matrix
print(spiralOrder(matrix4))  # Expected: [1, 2, 4, 3]