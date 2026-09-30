class Solution:
    def maxArea(self, height: list[int]) -> int:
        # area = height * width 
        # maximize area => maximize height, maximize width

        # height = min(height[i], height[j])
        # width = j - i + 1 

        i, j = 0, len(height)-1

        maxArea = 0 

        while i < j:
            area = min(height[i], height[j]) * (j - i )
            maxArea = max(area, maxArea)
            if height[i] < height[j]:
                i += 1 
            else:
                j -= 1 
        return maxArea

            
