# https://leetcode.com/problems/kth-largest-element-in-a-stream/

import heapq

class KthLargest:
    # O(NLogN), where N is len of Nums
    def __init__(self, k: int, nums: list[int]):
        # Initialize the min-heap and k value
        self.k = k
        self.min_heap = nums

        # Add initial elements to the heap
        heapq.heapify(self.min_heap) # O(N)
        while len(self.min_heap) > k: # O(N-K)LogN
            heapq.heappop(self.min_heap)

    # O(LogK)
    def add(self, val: int) -> int:
        # Add the new value to the heap
        heapq.heappush(self.min_heap, val) # O(LogK)

        # If heap size exceeds k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap) # O(LogK)

        # Return the kth largest element (root of min-heap)
        return self.min_heap[0]


# Test cases
def run_test_case(operations, inputs):
    results = []
    kth_largest = None

    for i, op in enumerate(operations):
        if op == "KthLargest":
            k, nums = inputs[i]
            kth_largest = KthLargest(k, nums)
            results.append(None)
        elif op == "add":
            results.append(kth_largest.add(inputs[i][0]))

    return results


# Example 1
operations1 = ["KthLargest", "add", "add", "add", "add", "add"]
inputs1 = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
print("Example 1 output:", run_test_case(operations1, inputs1))
# Expected: [null, 4, 5, 5, 8, 8]

# Example 2
operations2 = ["KthLargest", "add", "add", "add", "add"]
inputs2 = [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]
print("Example 2 output:", run_test_case(operations2, inputs2))
# Expected: [null, 7, 7, 7, 8]

# You can add your own test case here