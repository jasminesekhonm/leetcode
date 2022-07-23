class Solution:
    def maxArea(self, height: List[int]) -> int:
        # (j - i) * min(height[i], height[j])
        
        i = 0
        j = len(height) - 1
        
        maxArea = 0
        
        while i <= j:
            area_ = (j - i) * min(height[i], height[j])
            maxArea = max(maxArea, area_)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea
        
