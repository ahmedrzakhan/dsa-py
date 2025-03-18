# https://leetcode.com/problems/top-k-frequent-elements/description/

from collections import Counter
import heapq

# TC - O(NLogK), SC - O(N)
def topKFrequent(nums, k):
    # Count frequency of each number
    count = Counter(nums)

    # Use heap to get k most frequent elements
    # heapq.nlargest returns the k largest elements based on the frequency
    return heapq.nlargest(k, count.keys(), key=count.get)

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