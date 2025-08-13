# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# TC - O(N), SC - O(1)
def twoSum(A: list[int], target: int) -> list[int]:
    L = 0
    R = len(A) - 1

    while L < R:
        curr_sum = A[L] + A[R]
        if curr_sum == target:
            # Adding 1 to convert from 0-indexed to 1-indexed
            return [L + 1, R + 1]
        elif curr_sum < target:
            # If sum is too small, move left pointer to increase the sum
            L += 1
        else:
            # If sum is too large, move right pointer to decrease the sum
            R -= 1

    # The problem guarantees a solution, so this should never be reached
    return []

# Test cases
test_cases = [
    ([2,7,11,15], 9),
    ([2,3,4], 6),
    ([-1,0], -1)
]

for numbers, target in test_cases:
    result = twoSum(numbers, target)
    print(f"Input: numbers = {numbers}, target = {target}")
    print(f"Output: {result}\n")