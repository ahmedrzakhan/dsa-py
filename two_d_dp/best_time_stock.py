# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# TC - O(N), SC - O(N)
def maxProfit(A):
   # Memoization cache: (day_index, can_buy_state) -> maximum_profit_from_this_point
   dp = {}  # key=(i, buying) val=max_profit

   def dfs(i, buying):
       # Base case: past the last day, no more profit possible
       if i >= len(A):
           return 0

       # Return cached result if already computed
       if (i, buying) in dp:
           return dp[(i, buying)]

       # Option 1: Do nothing today, move to next day with same state
       cooldown = dfs(i + 1, buying)

       if buying:  # Currently in "can buy" state
           # Option 2: Buy stock today at price A[i]
           # After buying, switch to "can sell" state tomorrow
           buy = dfs(i + 1, not buying) - A[i]
           # Choose the better option: buy today or wait
           dp[(i, buying)] = max(buy, cooldown)
       else:  # Currently in "can sell" state (own stock)
           # Option 2: Sell stock today at price A[i]
           # After selling, must skip next day (cooldown), then can buy again
           sell = dfs(i + 2, not buying) + A[i]
           # Choose the better option: sell today or wait
           dp[(i, buying)] = max(sell, cooldown)

       return dp[(i, buying)]

   # Start at day 0 in "can buy" state
   return dfs(0, True)



# Test with examples
def test_solution():
    # Example 1
    prices1 = [1, 2, 3, 0, 2]
    result1 = maxProfit(prices1)
    print(f"Example 1: prices = {prices1}")
    print(f"Maximum profit: {result1}")
    print("Explanation: Buy at 1, sell at 3 (+2), cooldown, buy at 0, sell at 2 (+2) = 4")
    print("Wait, let me recalculate...")
    print("Actually: Buy at 1, sell at 2 (+1), cooldown, buy at 0, sell at 2 (+2) = 3")
    print()

    # Example 2
    prices2 = [1]
    result2 = maxProfit(prices2)
    print(f"Example 2: prices = {prices2}")
    print(f"Maximum profit: {result2}")
    print()

    # Additional test cases
    prices3 = [2, 1, 4]
    result3 = maxProfit(prices3)
    print(f"Test 3: prices = {prices3}")
    print(f"Maximum profit: {result3}")
    print("Buy at 1, sell at 4 = +3")
    print()

    prices4 = [1, 2, 3, 4, 5]
    result4 = maxProfit(prices4)
    print(f"Test 4: prices = {prices4}")
    print(f"Maximum profit: {result4}")
    print("Buy at 1, sell at 2, cooldown, buy at 3, sell at 4, cooldown, can't buy at 5")
    print("Or: Buy at 1, sell at 5 = +4")

test_solution()