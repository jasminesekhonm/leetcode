class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [10,9,2,5,3,7,101,18]
        # [0, 1,2,3,4,5, 6,  7]
        # length of the longest increasing subsequence ending at index 0 is 1 
        # length of the longest increasing subsequence ending at index 1 is 1 
        # length of the longest increasing subsequence ending at index 2 is 1 
        # length of the longest increasing subsequence ending at index 3 is 2 nums[2] < nums[3] ; prev_max = nums[3]
        # length of the longest increasing subsequence ending at index 4 is 2 nums[2] < nums[4]
        # length of the longest increasing subsequence ending at index 5 is 3 nums[5] < nums[4] and prev_max 
        # length of the longest increasing subsequence ending at index 6 is 4 
        # length of the longest increasing subsequence ending at index 7 is 4 
        
        # dp + memoization
        
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
        
        
        
        
        
        
        
