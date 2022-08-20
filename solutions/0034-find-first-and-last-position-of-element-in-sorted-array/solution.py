class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        i = 0 
        startIdx, endIdx = -1, -1
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        
        if nums[-1] < target or nums[0] > target:
            return [-1, -1]

        while target > nums[i]:
            i += 1
        
        if target == nums[i]:
            startIdx = i 
            endIdx = i
            
        while i < len(nums) and target == nums[i]:
            endIdx = i 
            i += 1
        return startIdx, endIdx
            
        
            
            
