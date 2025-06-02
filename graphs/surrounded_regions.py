# https://leetcode.com/problems/surrounded-regions

# TC - O(R*C), SC - O(R*C)
def solve(grid):
    if not grid or not grid[0]:
        return

    ROWS = len(grid)
    COLS = len(grid[0])

    # Helper function for DFS
    def dfs(R, C):
        if (R < 0 or R >= ROWS or C < 0 or C >= COLS or grid[R][C] != 'O'):
            return
        # Mark as visited by changing 'O' to '#'
        grid[R][C] = '#'
        # Explore all four directions
        dfs(R+1, C)  # Down
        dfs(R-1, C)  # Up
        dfs(R, C+1)  # Right
        dfs(R, C-1)  # Left

    # Step 1: Mark 'O' cells connected to edges as '#'
    # Check first and last rows
    for C in range(COLS):
        if grid[0][C] == 'O':
            dfs(0, C)
        if grid[ROWS-1][C] == 'O':
            dfs(ROWS-1, C)

    # Check first and last columns
    for R in range(ROWS):
        if grid[R][0] == 'O':
            dfs(R, 0)
        if grid[R][COLS-1] == 'O':
            dfs(R, COLS-1)

    # Step 2: Convert remaining 'O' to 'X', and '#' back to 'O'
    for R in range(ROWS):
        for C in range(COLS):
            if grid[R][C] == 'O':
                grid[R][C] = 'X'
            elif grid[R][C] == '#':
                grid[R][C] = 'O'

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