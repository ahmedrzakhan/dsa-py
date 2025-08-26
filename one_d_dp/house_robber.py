# https://leetcode.com/problems/house-robber/description/

# TC - O(N), SC - O(N)
def rob(A):
    if not A:
        return 0
    if len(A) == 1:
        return A[0]

    # dp[i] represents the maximum money that can be robbed up to house i
    dp = [0] * len(A)
    dp[0] = A[0]
    dp[1] = max(A[0], A[1])

    for i in range(2, len(A)):
        # Either rob the current house and add to dp[i-2], or skip it and take dp[i-1]
        dp[i] = max(dp[i-2] + A[i], dp[i-1])

    return dp[-1]

# Test cases
print(rob([100, 1, 1, 100]))  # Output: 200
print(rob([1,2,3,1]))  # Output: 4
print(rob([2,7,9,3,1]))  # Output: 12
print(rob([1,3,5,7]))  # Output: 8