# https://leetcode.com/problems/house-robber-ii/description/

# TC - O(N), SC - O(1)
def rob(A):
    if not A:
        return 0
    if len(A) == 1:
        return A[0]

    def rob_linear(arr):
        prev2 = prev1 = 0
        for num in arr:
            curr = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = curr
        return prev1

    # Case 1: Exclude last house (0 to n-2)
    # Case 2: Exclude first house (1 to n-1)
    return max(rob_linear(A[:-1]), rob_linear(A[1:]))

# Test cases for local execution
test_cases = [
    [2, 3, 2],      # Expected: 3
    [1, 2, 3, 1],   # Expected: 4
    [1, 2, 3],      # Expected: 3
]
for nums in test_cases:
    print(f"Input: {nums}, Output: {rob(nums)}")