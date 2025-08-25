from collections import defaultdict
import heapq

# TC - O(ELogV), SC - O(V+E)
def findCheapestPrice(n, flights, src, dst, k):
    # Alternative solution using Bellman-Ford algorithm.
    # More intuitive for this specific problem.
    # Initialize distances
    # dist[i] = minimum cost to reach city i
    dist = [float('inf')] * n
    dist[src] = 0

    # Relax edges at most k+1 times (k stops = k+1 edges)
    for _ in range(k + 1):
        temp_dist = dist[:]  # Copy current distances

        for from_city, to_city, price in flights:
            if dist[from_city] != float('inf'):
                temp_dist[to_city] = min(temp_dist[to_city], dist[from_city] + price)

        dist = temp_dist

    if dist[dst] != float('inf'):
        return dist[dst]
    else:
        return -1

# Example 1
n1 = 4
flights1 = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src1, dst1, k1 = 0, 3, 1
print(findCheapestPrice(n1, flights1, src1, dst1, k1))  # Output: 700

# Example 2
n2 = 3
flights2 = [[0,1,100],[1,2,100],[0,2,500]]
src2, dst2, k2 = 0, 2, 1
print(findCheapestPrice(n2, flights2, src2, dst2, k2))  # Output: 200

# Example 3
n3 = 3
flights3 = [[0,1,100],[1,2,100],[0,2,500]]
src3, dst3, k3 = 0, 2, 0
print(findCheapestPrice(n3, flights3, src3, dst3, k3))  # Output: 500