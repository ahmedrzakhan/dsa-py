# https://leetcode.com/problems/min-cost-to-connect-all-points/

import heapq

# TC - O(N^2LogN), SC - O(N^2)
def minCostConnectPoints(points):
    # Find minimum cost to connect all points using Manhattan distance.
    # Uses Prim's algorithm to build Minimum Spanning Tree.
    # Args:
    #     points: List of [x, y] coordinates
    # Returns:
    #     Minimum cost to connect all points
    N = len(points)
    if N <= 1:
        return 0

    def manhattan_distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    # Prim's algorithm
    visited = set()
    # Min-heap: (cost, point_index)
    heap = [(0, 0)]  # Start from point 0 with cost 0
    total_cost = 0

    while heap and len(visited) < N:
        cost, point_idx = heapq.heappop(heap)

        # Skip if already visited
        if point_idx in visited:
            continue

        # Add this point to MST
        visited.add(point_idx)
        total_cost += cost

        # Add all edges from this point to unvisited points
        current_point = points[point_idx]
        for i in range(N):
            if i not in visited:
                edge_cost = manhattan_distance(current_point, points[i])
                heapq.heappush(heap, (edge_cost, i))

    return total_cost

# Test case 1
points1 = [[0,0], [2,2], [3,10], [5,2], [7,0]]
print(minCostConnectPoints(points1))  # Output: 20

# Test case 2
points2 = [[3,12], [-2,5], [-4,1]]
print(minCostConnectPoints(points2))  # Output: 18