class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums) 
        
        dp = nums 
        
        for i in reversed(range(n-2)):
            dp[i] += max(dp[i+2:])
            
        return max(dp)
            
        
            
