class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            max_dp = 0
            for j in range(i):
                if nums[j] < nums[i] and dp[j] >= max_dp:
                    max_dp = dp[j]
            dp[i] = dp[i] + max_dp 
        return max(dp)
                
                
        
