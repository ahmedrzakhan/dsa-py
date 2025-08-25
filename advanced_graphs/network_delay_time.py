# https://leetcode.com/problems/network-delay-time/

from collections import defaultdict
import heapq

# TC - O(ELogN), SC - O(N+E)
def networkDelayTime(times, n, k):
    # Build adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    # Dijkstra's algorithm using min-heap
    # Format: (distance, node)
    min_heap = [(0, k)]
    distances = {}

    while min_heap:
        dist, node = heapq.heappop(min_heap)

        # Skip if we've already found a shorter path to this node
        if node in distances:
            continue

        # Record the shortest distance to this node
        distances[node] = dist

        # Explore neighbors
        for neighbor, weight in graph[node]:
            if neighbor not in distances:
                heapq.heappush(min_heap, (dist + weight, neighbor))

    # Check if all nodes are reachable
    if len(distances) != n:
        return -1

    # Return the maximum distance (time for last node to receive signal)
    return max(distances.values())

# Example 1
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2
print(networkDelayTime(times, n, k))  # Output: 2

# Example 2
times = [[1,2,1]]
n = 2
k = 1
print(networkDelayTime(times, n, k))  # Output: 1

# Example 3
times = [[1,2,1]]
n = 2
k = 2
print(networkDelayTime(times, n, k))  # Output: -1