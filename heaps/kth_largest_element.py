# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq

# TC - O(NLogK), SC - O(K)
# Approach 1: Using a min-heap of size k
def findKthLargest(nums, k):
    min_heap = []

    # Build a min-heap of size k
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    # The root of the heap will be the kth largest element
    return min_heap[0]


test_cases = [
        {'nums': [3, 2, 1, 5, 6, 4], 'k': 2, 'expected': 5},
        {'nums': [3, 2, 3, 1, 2, 4, 5, 5, 6], 'k': 4, 'expected': 4},
        {'nums': [1], 'k': 1, 'expected': 1},
        {'nums': [7, 6, 5, 4, 3, 2, 1], 'k': 5, 'expected': 3}
    ]

for i, test in enumerate(test_cases):
        result_heap = findKthLargest(test['nums'], test['k'])

        print(f"Test {i+1}:")
        print(f"  Input: nums = {test['nums']}, k = {test['k']}")
        print(f"  Expected: {test['expected']}")
        print(f"  Result (Heap): {result_heap}")