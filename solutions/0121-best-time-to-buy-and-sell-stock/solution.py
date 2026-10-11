class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        min_buy_price = float('inf')
        max_profit = 0 

        for price in prices:
            max_profit = max(max_profit, price-min_buy_price)
            min_buy_price = min(min_buy_price, price)

        return max_profit 
