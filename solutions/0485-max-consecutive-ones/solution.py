class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen = 0
        i = 0
        while i < len(nums):
            currLen = 0
            while i < len(nums) and nums[i] == 1:
                currLen += 1
                maxLen = max(maxLen, currLen)
                i += 1
            i += 1
        return maxLen
        
