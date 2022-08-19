class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0,0,1,1,1,2,2,3,3,4]
        
        
        i = 0
        while i+1 < len(nums):
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
        
                
            
            
            
