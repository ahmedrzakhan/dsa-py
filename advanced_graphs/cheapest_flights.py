from collections import defaultdict
import heapq

# TC - O(ELogV), SC - O(V+E)
def findCheapestPrice(n, flights, src, dst, k):
    # Create adjacency list
    graph = defaultdict(list)
    for start, end, price in flights:
        graph[start].append((end, price))

    # Priority queue: (price, node, stops)
    pq = [(0, src, 0)]

    # Track visited nodes with stops: (node, stops)
    visited = {}

    while pq:
        price, node, stops = heapq.heappop(pq)

        # If we reached destination
        if node == dst:
            return price

        # If we can still make stops
        if stops <= k:
            for next_node, next_price in graph[node]:
                new_price = price + next_price
                # Only add to queue if we haven't seen this node with same or fewer stops
                # or if we found a cheaper price for same stops
                if (next_node, stops + 1) not in visited or new_price < visited[(next_node, stops + 1)]:
                    visited[(next_node, stops + 1)] = new_price
                    heapq.heappush(pq, (new_price, next_node, stops + 1))

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