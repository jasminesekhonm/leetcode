class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0


        curr_sum = max_sum = nums[0]
        # [-2,1,-3,4,-1,2,1,-5,4]
        # -2
        # -1 [-2, 1]
        # -3, [5, 4, -1]
        # 
        for num in nums[1:]:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_sum)

        return max_sum
        
