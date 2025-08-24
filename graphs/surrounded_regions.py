# https://leetcode.com/problems/surrounded-regions

# TC - O(R*C), SC - O(R*C)
def solve(M):
    if not M or not M[0]:
        return

    ROWS = len(M)
    COLS = len(M[0])

    # Helper function for DFS
    def dfs(R, C):
        if (R < 0 or R >= ROWS or C < 0 or C >= COLS or M[R][C] != 'O'):
            return
        # Mark as visited by changing 'O' to '#'
        M[R][C] = '#'
        # Explore all four directions
        dfs(R+1, C)  # Down
        dfs(R-1, C)  # Up
        dfs(R, C+1)  # Right
        dfs(R, C-1)  # Left

    # Step 1: Mark 'O' cells connected to edges as '#'
    # Check first and last rows
    for C in range(COLS):
        if M[0][C] == 'O':
            dfs(0, C)
        if M[ROWS-1][C] == 'O':
            dfs(ROWS-1, C)

    # Check first and last columns
    for R in range(ROWS):
        if M[R][0] == 'O':
            dfs(R, 0)
        if M[R][COLS-1] == 'O':
            dfs(R, COLS-1)

    # Step 2: Convert remaining 'O' to 'X', and '#' back to 'O'
    for R in range(ROWS):
        for C in range(COLS):
            if M[R][C] == 'O':
                M[R][C] = 'X'
            elif M[R][C] == '#':
                M[R][C] = 'O'

# Example usage
# Example 1
grid1 = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
print("Before:")
for row in grid1:
    print(row)
solve(grid1)
print("After:")
for row in grid1:
    print(row)

# Example 2
grid2 = [["X"]]
print("\nBefore:")
for row in grid2:
    print(row)
solve(grid2)
print("After:")
for row in grid2:
    print(row)