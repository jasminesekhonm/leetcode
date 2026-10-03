class Solution:
    def maxProduct(self, nums: list[int]) -> int:

        n = len(nums)

        curr_max = curr_min = res = nums[0]

        for num in nums[1:]:
            tmp = curr_max * num 
            curr_max = max(tmp, curr_min * num, num)
            curr_min = min(tmp, curr_min * num, num)

            res = max(res, curr_max)
        
        return res 
        
