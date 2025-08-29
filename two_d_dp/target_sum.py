# https://leetcode.com/problems/target-sum/

from collections import defaultdict

# TC - O(N*M), SC - O(M) n is the length of the array nums and m is the sum of all the elements in the array.
def findTargetSumWays(nums, target):
    dp = defaultdict(int)
    dp[0] = 1

    for num in nums:
        next_dp = defaultdict(int)
        for total, count in dp.items():
            next_dp[total + num] += count
            next_dp[total - num] += count
        dp = next_dp

    return dp[target]



nums = [1, 1, 1, 1, 1]
target = 3
result = findTargetSumWays(nums, target)
print(f"Input: nums = {nums}, target = {target}")
print(f"Output: {result}")

# Show the actual expressions for the first example
print(f"\nThe {result} expressions are:")
expressions = [
    "-1 + 1 + 1 + 1 + 1 = 3",
    "+1 - 1 + 1 + 1 + 1 = 3",
    "+1 + 1 - 1 + 1 + 1 = 3",
    "+1 + 1 + 1 - 1 + 1 = 3",
    "+1 + 1 + 1 + 1 - 1 = 3"
]
for expr in expressions:
    print(expr)