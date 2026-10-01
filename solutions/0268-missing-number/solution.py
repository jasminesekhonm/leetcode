class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        i = 0 

        while i in set(nums):
            i += 1 
        return i
        
