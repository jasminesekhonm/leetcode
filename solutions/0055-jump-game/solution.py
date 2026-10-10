class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        target = len(nums)-1
        for i in range(n-2,-1,-1):
            if i + nums[i] >= target:
                target = i

        return True if target == 0 else False
        
        
            





