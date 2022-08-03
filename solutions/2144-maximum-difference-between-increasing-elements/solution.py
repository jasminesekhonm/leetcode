class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minElem = nums[0]
        maxDiff = -1
        for i in range(1, len(nums)):
            
            minElem = min(minElem, nums[i])
            if nums[i] != minElem:
                maxDiff = max(maxDiff, nums[i] - minElem)
        
        return maxDiff
            
        
