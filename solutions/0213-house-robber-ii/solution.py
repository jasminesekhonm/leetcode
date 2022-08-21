class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0 
        if len(nums) == 1:
            return nums[0]
        
        return max(self.robSimple(nums[:-1]), self.robSimple(nums[1:]))
        
    def robSimple(self, nums: List[int]) -> int:
        dp = nums
        n = len(nums)
        for i in reversed(range(n-2)):
            dp[i] += max(dp[i+2:])
        
        return max(dp)
