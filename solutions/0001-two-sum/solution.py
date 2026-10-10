class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        complements = {}

        for i, num in enumerate(nums):
            complement = target-num 
            if complement in complements:
                return [complements[complement], i]
            complements[num] = i 

        return [-1,-1]
