# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq

# TC - O(KLogN), SC - O(N)
def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    # Create a min-heap of points based on their distance from origin
    min_heap = []
    for x, y in points:
        # Calculate Euclidean distance squared (no need for sqrt as relative order is same)
        dist = x*x + y*y
        # Push (distance, x, y) to heap
        heapq.heappush(min_heap, (dist, x, y))

    # Extract k closest points from heap
    result = []
    for _ in range(k):
        dist, x, y = heapq.heappop(min_heap)
        result.append([x, y])

    return result

#   max_heap = []
#     for p in points:
#         x, y = p
#         val = (x*x) + (y*y)
#         heapq.heappush(max_heap, (-val, x, y))
#         if len(max_heap) > k:
#             heapq.heappop(max_heap)
#     res = []
#     while len(max_heap) >= 1:
#         _, x, y = heapq.heappop(max_heap)
#         res.append([x, y])
#    return res

# Test with Example 1
points1 = [[1,3],[-2,2]]
k1 = 1
print(f"Example 1 Input: points = {points1}, k = {k1}")
print(f"Output: {kClosest(points1, k1)}")

# Test with Example 2
points2 = [[3,3],[5,-1],[-2,4]]
k2 = 2
print(f"\nExample 2 Input: points = {points2}, k = {k2}")
print(f"Output: {kClosest(points2, k2)}")