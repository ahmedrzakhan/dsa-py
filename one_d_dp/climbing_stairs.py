# https://leetcode.com/problems/climbing-stairs/

# TC - O(N), SC - O(N)
def climbStairs(n: int) -> int:
    if n <= 2:
        return n

    # Initialize array to store number of ways for each step
    dp = [0] * (n + 1)
    dp[1] = 1  # One way to climb 1 step
    dp[2] = 2  # Two ways to climb 2 steps

    # Calculate ways for each step from 3 to n
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

test_cases = [2, 3, 5]
for n in test_cases:
    print(f"Number of ways to climb {n} steps: {climbStairs(n)}")