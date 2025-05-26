# https://leetcode.com/problems/min-cost-climbing-stairs/

# TC - O(N), SC - O(N)
def minCostClimbingStairs(cost):
    n = len(cost)
    # dp[i] represents the minimum cost to reach step i
    dp = [0] * (n + 1)

    # Base cases: starting from index 0 or 1
    # We don't need to initialize dp[0] or dp[1] as they are 0
    # Compute minimum cost for each step
    for i in range(2, n + 1):
        # To reach step i, you can come from step i-1 or i-2
        # Pay the cost at the step you come from
        dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

    return dp[n]

# Test case 1
cost1 = [10, 15, 20]
print(minCostClimbingStairs(cost1))  # Output: 15

# Test case 2
cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
print(minCostClimbingStairs(cost2))  # Output: 6