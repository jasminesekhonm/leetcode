class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        n = len(nums)

        if n <= 1:
            return n

        dp = [0] * n 

        for i in range(n):
            max_last = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_last = max(max_last, dp[j])
            dp[i] = max_last + 1

        return max(dp)


