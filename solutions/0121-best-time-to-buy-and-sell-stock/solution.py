class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minprice = prices[0]
        maxProfit = 0 
        for price in prices[1:]:
            maxProfit = max(maxProfit, price-minprice)
            minprice = min(price, minprice)
        
        return maxProfit


