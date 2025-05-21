# https://leetcode.com/problems/last-stone-weight/description/

import heapq

# TC - O(NLogN), SC - O(N)
def lastStoneWeight(stones):
    # Convert to negative values for max heap (Python only has min heap)
    stones = [-s for s in stones]
    heapq.heapify(stones)

    # Continue until 0 or 1 stone remains
    while len(stones) > 1:
        # Get the two heaviest stones
        first = -heapq.heappop(stones)
        second = -heapq.heappop(stones)

        # Smash them
        if first > second:
            # Add the remaining weight back to the heap
            heapq.heappush(stones, -(first - second))
        # If they're equal, both stones are destroyed (do nothing)

    # Return the last stone's weight or 0 if none remain
    return -stones[0] if stones else 0

# Test cases
test_cases = [
    [2, 7, 4, 1, 8, 1],
    [1],
    [2, 2],
    [3, 7, 2],
    [1, 3, 5, 7, 9]
]

# Run all test cases
for i, stones in enumerate(test_cases):
    result = lastStoneWeight(stones)
    print(f"Test case {i+1}: {stones}")
    print(f"Result: {result}")
    print("-" * 30)