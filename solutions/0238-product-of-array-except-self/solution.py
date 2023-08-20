class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for i in range(len(nums))]
        cum_product = 1
        for i in range(1, len(nums)):
            cum_product = cum_product * nums[i-1]
            ans[i] *= cum_product 
        
        cum_product = 1
        for i in range(len(nums)-2,-1,-1):
            cum_product *=nums[i+1]
            ans[i]*=cum_product
        
        return ans
