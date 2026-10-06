class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        complements = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complements:
                return [complements[complement], i] 
            complements[nums[i]] = i 
        
        return [-1, -1]
        

            
