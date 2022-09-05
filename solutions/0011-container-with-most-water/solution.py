class Solution:
    def maxArea(self, height: List[int]) -> int:
        # between any two height indices i, j
        # min(height[i], height[j]) * abs(j - i)
        
        i, j = 0, len(height)-1
        maxArea = 0
        while i <= j:
            currArea = min(height[i], height[j]) * (j-i)
            maxArea = max(currArea, maxArea)
            if min(height[i], height[j]) == height[j]:
                j -=1
            else:
                i += 1
        return maxArea
        
        
