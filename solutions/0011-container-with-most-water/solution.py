class Solution:
    def maxArea(self, height: List[int]) -> int:
        # height has at least 2 elements 
        
        # horizontal
        # integers 
        
        # width * height
        # farthest and/or the most height
        # (j - i) * min(height[i], height[j])
        
        # how do i initialize/move the pointers 
        # [1,8,6,2,5,4,8,3,7]
        # [0,1,2,3,4,5,6,7,8]
        # 1, 7 --> (8) * 1 = 8 
        # 
        
        i = 0 
        j = len(height) - 1
        
        maxAmount = 0
        
        while i < j:
            amount = (j - i) * min(height[i], height[j])
            maxAmount = max(amount, maxAmount)
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        
        return maxAmount
                
            
            
        
    
            
        
        
        
        
