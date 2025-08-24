# https://leetcode.com/problems/number-of-islands

# TC - O(M*N), SC - O(M*N)
def numIslands(M):
    if not M:
        return 0

    ROWS = len(M)
    COLS = len(M[0])
    count = 0

    def dfs(R, C):
        # Check if current position is out of bounds or not land
        if R < 0 or R >= ROWS or C < 0 or C >= COLS or M[R][C] != "1":
            return
        # Mark as visited by changing to '0'
        M[R][C] = "0"
        # Explore all four directions
        dfs(R+1, C)  # Down
        dfs(R-1, C)  # Up
        dfs(R, C+1)  # Right
        dfs(R, C-1)  # Left

    # Iterate through each cell in the M
    for i in range(ROWS):
        for j in range(COLS):
            if M[i][j] == "1":
                count += 1
                dfs(i, j)  # Mark all connected land as visited

    return count

# Test cases
# Example 1
M1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
print(numIslands(M1))  # Output: 1

# Example 2
M2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(numIslands(M2))  # Output: 3