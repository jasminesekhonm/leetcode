class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        
        if len(nums) == 1:
            return True 
        
        i = 0
        max_index = nums[i]
        while i < len(nums) and i <= max_index:
            new_index = nums[i] + i 
            max_index = max(max_index, new_index)
            i += 1
        return True if i == len(nums) else False
