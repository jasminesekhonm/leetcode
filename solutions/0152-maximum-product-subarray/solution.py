class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curr_max = curr_min = ans = nums[0]

        for num in nums[1:]:
            tmp = curr_max * num 
            curr_max = max(curr_min * num, tmp, num)
            
            curr_min = min(curr_min * num, tmp, num)
            ans = max(ans, curr_max)
          
        return ans


