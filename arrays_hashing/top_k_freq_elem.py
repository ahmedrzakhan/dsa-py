# https://leetcode.com/problems/top-k-frequent-elements/description/

from collections import Counter
import heapq

# TC - O(NLogK), SC - O(N)
def topKFrequent(nums, k):
    # Solution 1: Using Min Heap
    # Time: O(n log k), Space: O(n)
    # Count frequencies
    counter = Counter(nums)

    # Use min heap to keep track of top k elements
    min_heap = []

    for num, freq in counter.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Extract elements from heap
    return [num for _, num in min_heap]

# TC - O(NLogN), SC - O(N)
def topKFrequent_sorting(nums, k):
    # Count frequency of each number
    count = Counter(nums)

    # Sort by frequency (descending) and value (ascending) if needed
    # Take first k elements
    return [num for num, _ in sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]]

# Test cases
print(topKFrequent([1,1,1,2,2,3], 2))  # Output: [1,2]
print(topKFrequent([1], 1))           # Output: [1]

print(topKFrequent_sorting([1,1,1,2,2,3], 2))  # Output: [1,2]
print(topKFrequent_sorting([1], 1))           # Output: [1]