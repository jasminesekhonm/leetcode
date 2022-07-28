class Solution:
    def trap(self, height: List[int]) -> int:
        
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        # [0, len(height)] 
        # 
        
        i = 0 
        j = len(height) - 1
        
        # h1, h2 
        
        area = 0
        i = 1
        j = len(height) - 2
        
        h1 = [0 for _ in range(len(height))]
        h2 = [0 for _ in range(len(height))]
        
        h1[0] = height[0]
        
        h2[len(height) - 1] = height[len(height) - 1]
        
        while i < len(height) and j >= 0:
            h1[i] = max(h1[i - 1], height[i])
            h2[j] = max(h2[j + 1], height[j])
            i = i + 1
            j = j - 1
            
        for i in range(len(height)):
            area = area + max(min(h1[i], h2[i]) - height[i], 0)
        return area
        
            
            
