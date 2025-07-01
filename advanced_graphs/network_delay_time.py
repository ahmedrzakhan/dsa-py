# https://leetcode.com/problems/network-delay-time/

from collections import defaultdict
import heapq

# TC - O(ELogN), SC - O(N+E)
def networkDelayTime(times, n, k):
    # Build adjacency list
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    # Initialize distances
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0

    # Min-heap for Dijkstra's algorithm
    pq = [(0, k)]  # (distance, node)
    visited = set()

    while pq:
        d, u = heapq.heappop(pq)

        if u in visited:
            continue

        visited.add(u)

        # Explore neighbors
        for v, w in graph[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (d + w, v))

    # Check if all nodes are reachable
    if len(visited) < n:
        return -1

    # Return maximum distance
    return max(dist.values())

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