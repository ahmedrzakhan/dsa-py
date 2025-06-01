# https://neetcode.io/problems/islands-and-treasure

# TC - O(M*N), SC - O(M*N)
def updateTreasureDistance(grid):
    if not grid or not grid[0]:
        return grid

    ROWS, COLS = len(grid), len(grid[0])
    INF = 2147483647
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    queue = []

    # Initialize: find all treasure chests (0) and add to queue
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 0:
                queue.append((i, j))

    # BFS to update distances
    distance = 0
    while queue:
        distance += 1
        for _ in range(len(queue)):
            R, C = queue.pop(0)
            for ROW, COL in directions:
                DR, DC = R + ROW, C + COL
                if 0 <= DR < ROWS and 0 <= DC < COLS and grid[DR][DC] == INF:
                    grid[DR][DC] = distance
                    queue.append((DR, DC))

    return grid

# Test the function
# Example 1
grid1 = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]
result1 = updateTreasureDistance(grid1)
for row in result1:
    print(row)

# Example 2
grid2 = [
    [0, -1],
    [2147483647, 2147483647]
]
result2 = updateTreasureDistance(grid2)
for row in result2:
    print(row)