# https://leetcode.com/problems/rotting-oranges

# TC - O(M*N), SC - O(M*N)
def orangesRotting(M):
    if not M or not M[0]:
            return 0

    ROWS, COLS = len(M), len(M[0])
    fresh = 0
    queue = []

    # Count fresh oranges and find initial rotten ones
    for i in range(ROWS):
        for j in range(COLS):
            if M[i][j] == 1:
                fresh += 1
            elif M[i][j] == 2:
                queue.append([i, j])

    if fresh == 0:
        return 0

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    minutes = 0

    while queue and fresh > 0:
        queueLength = len(queue)

        # Process all rotten oranges at current time
        for _ in range(queueLength):
            cell = queue.pop(0)  # Use popleft() for proper BFS

            for dir in directions:
                nextRow, nextCol = cell[0] + dir[0], cell[1] + dir[1]

                if (nextRow < 0 or nextRow >= ROWS or
                    nextCol < 0 or nextCol >= COLS):
                    continue

                if M[nextRow][nextCol] == 1:
                    M[nextRow][nextCol] = 2
                    fresh -= 1
                    queue.append([nextRow, nextCol])

        # Increment time after processing all current rotten oranges
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
