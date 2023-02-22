class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxOnes = 0 

        i = 0 
        while i < len(nums):
            currOnes = 0 
            while i < len(nums) and nums[i] == 1:
                currOnes += 1
                maxOnes = max(maxOnes, currOnes)
                i += 1 
            i += 1 
        return maxOnes  

