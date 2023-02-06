class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = -float('inf')

        i, j = 0, len(heights)-1

        while i < j:
            currArea = (j - i) * min(heights[i], heights[j])
            maxArea = max(currArea, maxArea)
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        
        return maxArea

