# https://leetcode.com/problems/rotting-oranges

# TC - O(M*N), SC - O(M*N)
def orangesRotting(grid):
    if not grid or not grid[0]:
        return 0

    ROWS, COLS = len(grid), len(grid[0])
    fresh = 0
    queue = []

    # First pass to count fresh oranges and enqueue rotten oranges
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                fresh += 1
            elif grid[i][j] == 2:
                queue.append([i, j])

    if fresh == 0:
        return 0

    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    minutes = 0

    # BFS
    while queue:
        queueLength = len(queue)
        rottenSpread = False
        for i in range(queueLength):
            cell = queue.pop(0)
            for dir in directions:
                nextRow, nextCol = cell[0] + dir[0], cell[1] + dir[1]
                if nextRow < 0 or nextRow >= ROWS or nextCol < 0 or nextCol >= COLS:
                    continue
                if grid[nextRow][nextCol] == 1:
                    grid[nextRow][nextCol] = 2
                    fresh -= 1
                    queue.append([nextRow, nextCol])
                    rottenSpread = True
        if rottenSpread:
            minutes += 1

    if fresh == 0:
        return minutes
    return -1

grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1],
]
result = orangesRotting(grid)
print(f"Minutes until all oranges rot: {result}")

grid2 = [
    [2, 1, 1],
    [0, 1, 1],
    [1, 0, 1],
]
result2 = orangesRotting(grid2)
print(f"Minutes until all oranges rot: {result2}")

grid3 = [
    [0, 2],
]
result3 = orangesRotting(grid3)
print(f"Minutes until all oranges rot: {result3}")
