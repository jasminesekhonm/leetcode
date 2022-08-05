class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        # [2,7,11,15]
        # complement[7] = 0 
        
        for i in range(len(nums)):
            if nums[i] in complement:
                return [i, complement[nums[i]]]
            
            complement[target - nums[i]] = i 
            
