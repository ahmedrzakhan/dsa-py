# https://leetcode.com/problems/walls-and-gates/description/
# https://neetcode.io/problems/islands-and-treasure

from typing import List

def islandsAndTreasure(M: List[List[int]]) -> None:
    # You have a m x n 2D M initialized with these three possible values:
    # -1: A wall or an obstacle.
    # 0: A treasure chest.
    # INF: An empty room (represented as 2147483647).

    # Fill each empty room with the distance to its nearest treasure chest.
    # If it is impossible to reach a treasure chest, the room should remain filled with INF.
    if not M or not M[0]:
        return None

    ROWS, COLS = len(M), len(M[0])
    INF = 2147483647

    def dfs(R: int, C: int, distance: int) -> None:
        # Base cases
        if (R < 0 or R >= ROWS or
            C < 0 or C >= COLS or
            M[R][C] < distance):  # Already visited with shorter distance or is wall/treasure
            return

        # Update the current cell with the distance
        M[R][C] = distance
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up

        # Recursively explore all 4 directions
        for next_row, next_col in directions:
            dfs(R + next_row, C + next_col, distance + 1)

    # Start DFS from each treasure chest (0)
    for i in range(ROWS):
        for j in range(COLS):
            if M[i][j] == 0:
                dfs(i, j, 0)

def print_M(M: List[List[int]], title: str):
    """Helper function to print M in a readable format"""
    print(f"\n{title}:")
    INF = 2147483647
    for row in M:
        formatted_row = []
        for cell in row:
            if cell == INF:
                formatted_row.append("INF")
            elif cell == -1:
                formatted_row.append(" -1")
            else:
                formatted_row.append(f"{cell:3d}")
        print("[" + ", ".join(formatted_row) + "]")

# Test Cases
if __name__ == "__main__":
    INF = 2147483647

    # Test Case 1: Basic example
    print("=" * 50)
    print("TEST CASE 1: Basic M")
    M1 = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF]
    ]
    print_M(M1, "Before")
    islandsAndTreasure(M1)
    print_M(M1, "After")

    # Test Case 2: Single treasure
    print("\n" + "=" * 50)
    print("TEST CASE 2: Single Treasure")
    M2 = [
        [INF, INF, INF],
        [INF, 0, INF],
        [INF, INF, INF]
    ]
    print_M(M2, "Before")
    islandsAndTreasure(M2)
    print_M(M2, "After")

    # Test Case 3: No treasure
    print("\n" + "=" * 50)
    print("TEST CASE 3: No Treasure")
    M3 = [
        [INF, -1, INF],
        [-1, -1, -1],
        [INF, -1, INF]
    ]
    print_M(M3, "Before")
    islandsAndTreasure(M3)
    print_M(M3, "After")

    # Test Case 4: All walls
    print("\n" + "=" * 50)
    print("TEST CASE 4: All Walls")
    M4 = [
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, -1]
    ]
    print_M(M4, "Before")
    islandsAndTreasure(M4)
    print_M(M4, "After")

    # Test Case 5: Multiple treasures
    print("\n" + "=" * 50)
    print("TEST CASE 5: Multiple Treasures")
    M5 = [
        [0, INF, INF, 0],
        [INF, INF, INF, INF],
        [INF, INF, INF, INF],
        [0, INF, INF, 0]
    ]
    print_M(M5, "Before")
    islandsAndTreasure(M5)
    print_M(M5, "After")

    # Test Case 6: Edge case - single cell with treasure
    print("\n" + "=" * 50)
    print("TEST CASE 6: Single Cell with Treasure")
    M6 = [[0]]
    print_M(M6, "Before")
    islandsAndTreasure(M6)
    print_M(M6, "After")

    # Test Case 7: Isolated rooms
    print("\n" + "=" * 50)
    print("TEST CASE 7: Isolated Rooms")
    M7 = [
        [INF, -1, 0],
        [-1, -1, -1],
        [INF, -1, INF]
    ]
    print_M(M7, "Before")
    islandsAndTreasure(M7)
    print_M(M7, "After")