class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy lowest
        # sell highest 
        
        minPrice = float('inf')
        maxProfit = 0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        return maxProfit
                    
        
