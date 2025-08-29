def change(amount, coins):
    # Count the number of combinations that make up the given amount using coins.
    # Args: amount: Target amount of money
    #     coins: List of coin denominations (infinite supply of each)
    # Returns: Number of combinations to make up the amount
    # Time Complexity: O(amount * len(coins))
    # Space Complexity: O(amount)
    # dp[i] represents the number of ways to make amount i
    dp = [0] * (amount + 1)
    dp[0] = 1  # Base case: one way to make amount 0 (use no coins)

    # For each coin denomination
    for coin in coins:
        # Update dp array for all amounts from coin to target amount
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


def change_verbose(amount, coins):
    """
    Verbose version with detailed explanation of the algorithm.
    """
    print(f"Finding combinations for amount={amount}, coins={coins}")

    # Initialize dp array
    dp = [0] * (amount + 1)
    dp[0] = 1
    print(f"Initial dp: {dp}")

    # Process each coin
    for coin in coins:
        print(f"\nProcessing coin {coin}:")
        old_dp = dp.copy()

        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

        print(f"dp after coin {coin}: {dp}")
        print(f"Changes: {[dp[i] - old_dp[i] for i in range(len(dp))]}")

    print(f"\nFinal answer: {dp[amount]}")
    return dp[amount]


# Test cases
def test_solution():
    test_cases = [
        (5, [1, 2, 5]),  # Expected: 4
        (3, [2]),        # Expected: 0
        (10, [10]),      # Expected: 1
        (0, [1, 2]),     # Expected: 1 (edge case)
        (4, [1, 2, 3]),  # Expected: 4 ([1,1,1,1], [1,1,2], [2,2], [1,3])
    ]

    for amount, coins in test_cases:
        result = change(amount, coins)
        print(f"Amount: {amount}, Coins: {coins} -> {result} combinations")


    # Run test cases
test_solution()

print("\n" + "="*50)
print("Verbose example for amount=5, coins=[1,2,5]:")
change_verbose(5, [1, 2, 5])