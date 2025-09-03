# https://leetcode.com/problems/search-a-2d-matrix/description/

# TC - O(LogM + LogN)), SC - O(1)
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:  # Check if matrix is empty
        return False

    ROWS, COLS = len(matrix), len(matrix[0])

    TOP, BOT = 0, ROWS - 1
    while TOP <= BOT:
        ROW = (TOP + BOT) // 2
        if target > matrix[ROW][-1]:
            TOP = ROW + 1
        elif target < matrix[ROW][0]:
            BOT = ROW - 1
        else:
            break

    if not (TOP <= BOT):
        return False

    ROW = (TOP + BOT) // 2
    L, R = 0, COLS - 1
    while L <= R:
        mid = (L + R) // 2
        if matrix[ROW][mid] == target:
            return True
        elif matrix[ROW][mid] < target:
            L = mid + 1
        else:
            R = mid - 1
    return False

# Test cases
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(searchMatrix(matrix1, 3))  # Output: True
print(searchMatrix(matrix1, 13))  # Output: False