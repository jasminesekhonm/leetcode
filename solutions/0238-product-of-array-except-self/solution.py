class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        prod = 1 
        res = []

        for num in nums:
            res.append(prod)
            prod *= num 
        
        prod = 1

        for i in range(len(nums)-1,-1,-1):
            res[i] *= prod
            prod *= nums[i]


        return res


