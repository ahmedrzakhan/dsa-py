# https://leetcode.com/problems/pacific-atlantic-water-flow

# TC - O(R*C), SC - O(R*C)
def pacificAtlantic(M):
    if not M or not M[0]:
        return []

    ROWS, COLS = len(M), len(M[0])
    # Sets to track cells reachable from Pacific and Atlantic
    pacific = set()
    atlantic = set()

    def dfs(R, C, visited, prev_height):
        # Check boundaries, if already visited, or if height condition not met
        if (R < 0 or R >= ROWS or C < 0 or C >= COLS or
            (R, C) in visited or M[R][C] < prev_height):
            return
        visited.add((R, C))
        # Explore all four directions
        dfs(R + 1, C, visited, M[R][C])
        dfs(R - 1, C, visited, M[R][C])
        dfs(R, C + 1, visited, M[R][C])
        dfs(R, C - 1, visited, M[R][C])

    # Run DFS from Pacific borders (left edge and top edge)
    for R in range(ROWS):
        dfs(R, 0, pacific, float('-inf'))  # Left edge
    for C in range(COLS):
        dfs(0, C, pacific, float('-inf'))  # Top edge

    # Run DFS from Atlantic borders (right edge and bottom edge)
    for R in range(ROWS):
        dfs(R, COLS - 1, atlantic, float('-inf'))  # Right edge
    for C in range(COLS):
        dfs(ROWS - 1, C, atlantic, float('-inf'))  # Bottom edge

    # Find intersection of cells reachable from both oceans
    result = []
    for R in range(ROWS):
        for C in range(COLS):
            if (R, C) in pacific and (R, C) in atlantic:
                result.append([R, C])

    return result

# Test cases
    # Test case 1
heights1 = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]
print("Test 1 Input:", heights1)
print("Test 1 Output:", pacificAtlantic(heights1))

# Test case 2
heights2 = [[1]]
print("Test 2 Input:", heights2)
print("Test 2 Output:", pacificAtlantic(heights2))
