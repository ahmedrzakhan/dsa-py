# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List

# TC - O(N), SC - O(1)
def maxProfit(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Update minimum price seen so far
        min_price = min(min_price, price)
        # Calculate potential profit if we sell at current price
        curr_profit = price - min_price
        # Update maximum profit if current profit is larger
        max_profit = max(max_profit, curr_profit)

    return max_profit


prices1 = [7,1,5,3,6,4]

print(maxProfit(prices1))