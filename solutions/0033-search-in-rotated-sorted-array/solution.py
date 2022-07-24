class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # sorted
        # distinct values 
        
        if len(nums) == 0:
            return -1
        
        if len(nums) == 1 and nums[0] == target:
            return 0
                
        # [4,5,6,7,0,1,2] 
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        return -1 
