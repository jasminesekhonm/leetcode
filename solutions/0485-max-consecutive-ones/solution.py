class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        i = 0
        maxCount = 0
        
        currCount = 0
        while i < len(nums):
            while i < len(nums) and nums[i] == 1:
                i += 1
                currCount += 1
            maxCount = max(maxCount, currCount)
            currCount = 0
            i += 1
        return maxCount
