class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # idx: 0, 1, 2, 3 
        # num: 4, 3, 2, 1 

        # in this case 0 is missing 

        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num 
        
        return missing 
        
