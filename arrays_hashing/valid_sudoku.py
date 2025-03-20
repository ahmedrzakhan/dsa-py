# https://leetcode.com/problems/valid-sudoku/description/

# TC - O(N^2), SC - O(N^2)
def isValidSudoku(board):
    # Initialize sets to keep track of numbers in each row, column, and 3x3 box
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            # Skip empty cells
            if board[i][j] == '.':
                continue

            num = board[i][j]

            # Calculate box index (0-8)
            box_idx = (i // 3) * 3 + j // 3

            # Check if number already exists in current row, column, or 3x3 box
            if (num in rows[i] or
                num in cols[j] or
                num in boxes[box_idx]):
                return False

            # Add number to the respective sets
            rows[i].add(num)
            cols[j].add(num)
            boxes[box_idx].add(num)

    return True

# Test cases
board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print(isValidSudoku(board1))  # Should print: True
print(isValidSudoku(board2))  # Should print: False


# The box_idx formula is key:
# i // 3 gives us the row group (0, 1, or 2)
# j // 3 gives us the column group (0, 1, or 2)
# (i // 3) * 3 + j // 3 combines these to give a unique index (0-8) for each box

# ```python
# box_idx = (i // 3) * 3 + j // 3
# ```

# This formula is commonly used to calculate the index of a 3x3 box in a 9x9 grid (like in Sudoku). It takes a row index `i` and a column index `j` (both ranging from 0 to 8) and determines which of the 9 possible 3x3 boxes the position `(i, j)` belongs to. The boxes are numbered from 0 to 8, typically in this layout:

# ```
# 0 1 2
# 3 4 5
# 6 7 8
# ```

# ### Step-by-Step Explanation:

# 1. **`i // 3`: Row Group Calculation**
#    - The `//` operator is floor division in Python, which divides and rounds down to the nearest integer.
#    - `i` is the row index (0 to 8).
#    - Dividing `i` by 3 groups the rows into sets of 3:
#      - Rows 0, 1, 2 → `0 // 3 = 0`
#      - Rows 3, 4, 5 → `3 // 3 = 1`
#      - Rows 6, 7, 8 → `6 // 3 = 2`
#    - This tells us which "row of boxes" the position is in (top, middle, or bottom).

# 2. **`(i // 3) * 3`: Starting Box Index for the Row**
#    - Multiplying the result by 3 gives the starting box index for that row of boxes:
#      - If `i // 3 = 0` (rows 0-2) → `0 * 3 = 0` (boxes 0, 1, 2)
#      - If `i // 3 = 1` (rows 3-5) → `1 * 3 = 3` (boxes 3, 4, 5)
#      - If `i // 3 = 2` (rows 6-8) → `2 * 3 = 6` (boxes 6, 7, 8)
#    - This determines the first box in the row of 3x3 boxes.

# 3. **`j // 3`: Column Group Calculation**
#    - `j` is the column index (0 to 8).
#    - Dividing `j` by 3 groups the columns into sets of 3:
#      - Columns 0, 1, 2 → `0 // 3 = 0`
#      - Columns 3, 4, 5 → `3 // 3 = 1`
#      - Columns 6, 7, 8 → `6 // 3 = 2`
#    - This tells us which "column of boxes" the position is in (left, middle, or right).

# 4. **Adding Them Together: `(i // 3) * 3 + j // 3`**
#    - Combine the row group offset (`(i // 3) * 3`) with the column offset (`j // 3`) to get the final box index.
#    - The result is a number from 0 to 8, corresponding to one of the 9 boxes in the grid.

# ### Visual Example:
# Imagine a 9x9 grid divided into 3x3 boxes:
# ```
# Box 0 | Box 1 | Box 2
# ------+-------+------
# Box 3 | Box 4 | Box 5
# ------+-------+------
# Box 6 | Box 7 | Box 8
# ```

# - **Case 1: `i = 1, j = 2` (row 1, column 2)**:
#   - `i // 3 = 1 // 3 = 0`
#   - `(i // 3) * 3 = 0 * 3 = 0`
#   - `j // 3 = 2 // 3 = 0`
#   - `box_idx = 0 + 0 = 0`
#   - Result: Box 0 (top-left 3x3 box).

# - **Case 2: `i = 4, j = 5` (row 4, column 5)**:
#   - `i // 3 = 4 // 3 = 1`
#   - `(i // 3) * 3 = 1 * 3 = 3`
#   - `j // 3 = 5 // 3 = 1`
#   - `box_idx = 3 + 1 = 4`
#   - Result: Box 4 (middle-center 3x3 box).

# - **Case 3: `i = 7, j = 8` (row 7, column 8)**:
#   - `i // 3 = 7 // 3 = 2`
#   - `(i // 3) * 3 = 2 * 3 = 6`
#   - `j // 3 = 8 // 3 = 2`
#   - `box_idx = 6 + 2 = 8`
#   - Result: Box 8 (bottom-right 3x3 box).

# ### Why It Works:
# - The formula cleverly maps any `(i, j)` coordinate in a 9x9 grid to one of the 9 boxes by:
#   - Using `(i // 3)` to determine the vertical group (0, 1, or 2),
#   - Scaling it by 3 to jump to the correct row of boxes,
#   - Adding `(j // 3)` to shift horizontally within that row.

# This is a concise and efficient way to compute box indices without needing explicit conditionals or loops!