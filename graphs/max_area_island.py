# https://leetcode.com/problems/max-area-of-island

# TC - O(M*N), SC - O(M*N)
def maxAreaOfIsland(grid):
    if not grid:
        return 0

    ROWS, COLS = len(grid), len(grid[0])
    max_area = 0

    def dfs(R, C):
        # Check boundaries and if cell is land (1) and not visited
        if R < 0 or R >= ROWS or C < 0 or C >= COLS or grid[R][C] != 1:
            return 0

        # Mark as visited by changing value to 0
        grid[R][C] = 0
        count = 1

        # Explore all 4 directions
        count += dfs(R+1, C)  # down
        count += dfs(R-1, C)  # up
        count += dfs(R, C+1)  # right
        count += dfs(R, C-1)  # left

        return count

    # Iterate through each cell in the grid
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))

    return max_area

# Example 1
grid1 = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
print(maxAreaOfIsland(grid1))  # Output: 6

# Example 2
grid2 = [[0,0,0,0,0,0,0,0]]
print(maxAreaOfIsland(grid2))  # Output: 0