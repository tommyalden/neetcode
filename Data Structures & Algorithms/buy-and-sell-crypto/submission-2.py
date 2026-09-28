class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0

        for i, price in enumerate(prices):
            if prices[buy] > price: buy = i
            elif price - prices[buy] > profit: 
                profit = price - prices[buy]

        return profit


        