# https://leetcode.com/problems/coin-change

# NOTE: i respresents the amount of money

# TC - O(amount*N), SC - O(amount)
def coinChange(coins, amount):
    # Initialize dp array with amount + 1 (impossible value) since we want minimum
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # Base case: 0 amount requires 0 coins

    # Iterate through each amount from 1 to target amount
    for i in range(1, amount + 1):
        # Try each coin denomination
        for coin in coins:
            # If coin value <= current amount, we can use this coin
            if coin <= i:
                # Update minimum: current minimum vs (coins for remaining amount + 1)
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return result: -1 if impossible, otherwise minimum coins needed
    return dp[amount] if dp[amount] != amount + 1 else -1

# Test cases
print(coinChange([1, 2, 5], 11))  # Output: 3
print(coinChange([2], 3))         # Output: -1
print(coinChange([1], 0))         # Output: 0