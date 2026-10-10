class Solution:
    def rob(self, nums: list[int]) -> int:
        
        n = len(nums)

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0 for _ in range(n)]

        dp[0] = nums[0]

        dp[1] = nums[1]

        if len(nums) == 2:
            return max(dp)
            
        dp[2] = nums[2] + dp[0]

        for i in range(3,n):
            dp[i] = nums[i] + max(dp[i-2],dp[i-3])

        return max(dp)
