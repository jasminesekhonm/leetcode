class Solution:
    def trap(self, height: List[int]) -> int:
        leftMaxes = [0 for _ in height] 
        rightMaxes = [0 for _ in height]  

        leftMaxes[0] = height[0]
        rightMaxes[-1] = height[-1]
        
        for i in range(1, len(height)):
            leftMaxes[i] = max(leftMaxes[i-1], height[i])
        
        for i in range(len(height)-2,-1,-1):
            rightMaxes[i] = max(rightMaxes[i+1], height[i])

        total_water = 0 
        for i in range(len(height)):
            curr_water = min(rightMaxes[i], leftMaxes[i]) - height[i]
            total_water += curr_water

        return total_water


