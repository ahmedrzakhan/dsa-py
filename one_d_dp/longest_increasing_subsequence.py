# https://leetcode.com/problems/longest-increasing-subsequence

# TC - O(N^2), SC - O(N)
def lengthOfLIS(A):
    # LIS[i] represents the length of the longest increasing subsequence
    # ending at index i.
    if not A:
        return 0

    LIS = [1] * len(A)

    for i in range(len(A) - 1, -1, -1):
        for j in range(i + 1, len(A)):
            if A[i] < A[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    return max(LIS)

# Test cases
test_cases = [
    [10,9,2,5,3,7,101,18],
    [0,1,0,3,2,3],
    [7,7,7,7,7,7,7]
]

for nums in test_cases:
    print(f"Input: {nums}")
    print(f"Output: {lengthOfLIS(nums)}\n")