class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        n = len(nums)

        res = [1 for _ in range(n)]

        curr_prod = 1
        for i in range(n-1,0,-1):
            curr_prod*=nums[i]
            res[i-1] = curr_prod
        
        curr_prod = 1
        for i in range(n):
            res[i] *= curr_prod
            curr_prod *= nums[i]
        
        return res
