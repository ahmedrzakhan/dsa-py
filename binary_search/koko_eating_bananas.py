# https://leetcode.com/problems/koko-eating-bananas/description/

import math

# TC - O(N*LogM), SC - O(1)
def minEatingSpeed(piles, h):
    # Set the search boundaries
    L = 1  # minimum possible speed
    R = max(piles)  # maximum possible speed

    # Binary search
    while L < R:
        mid = (L + R) // 2
        total_time = 0

        # Calculate total hours needed at current speed
        for p in piles:
            total_time += math.ceil(p / mid)

        # If too slow (takes more hours than allowed)
        if total_time > h:
            L = mid + 1
        # If fast enough (within hours limit)
        else:
            R = mid

    return R

# Test cases
print(minEatingSpeed([3,6,7,11], 8))  # Output: 4
print(minEatingSpeed([30,11,23,4,20], 5))  # Output: 30
print(minEatingSpeed([30,11,23,4,20], 6))  # Output: 23)