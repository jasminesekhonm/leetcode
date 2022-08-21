class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1
        res = [1 for _ in range(n)]
        for i in range(n):
            res[i] *= prod
            prod *= nums[i]
        
        prod = 1
        for i in reversed(range(n)):
            res[i] *= prod
            prod *= nums[i]
        
        return res
            
            
            
            
