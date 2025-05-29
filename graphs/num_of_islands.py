# https://leetcode.com/problems/number-of-islands

# TC - O(M*N), SC - O(M*N)
def numIslands(grid):
    if not grid:
        return 0

    ROWS = len(grid)
    COLS = len(grid[0])
    count = 0

    def dfs(R, C):
        # Check if current position is out of bounds or not land
        if (R < 0 or R >= ROWS or C < 0 or C >= COLS or grid[R][C] != "1"):
            return
        # Mark as visited by changing to '0'
        grid[R][C] = "0"
        # Explore all four directions
        dfs(R+1, C)  # Down
        dfs(R-1, C)  # Up
        dfs(R, C+1)  # Right
        dfs(R, C-1)  # Left

    # Iterate through each cell in the grid
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == "1":
                count += 1
                dfs(i, j)  # Mark all connected land as visited

    return count

# Test cases
# Example 1
grid1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
print(numIslands(grid1))  # Output: 1

# Example 2
grid2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(numIslands(grid2))  # Output: 3