class Solution:
    def rob(self, nums: list[int]) -> int:

        dp = [0 for _ in range(len(nums))]

        if len(nums) <= 2:
            return max(nums)

        dp[0] = nums[0]
        dp[1] = nums[1]

        dp[2] = nums[2] + dp[0]

        for i in range(3, len(nums)):
            dp[i] = nums[i] + max(dp[i-2], dp[i-3])

        
        return max(dp)
        
