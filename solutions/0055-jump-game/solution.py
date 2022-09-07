class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [3,2,1,0,4]
        
        # 4: GOOD
        # 0: BAD 
        # 1: BAD
        # 2: BAD
        # 3: BAD
        
        # [2,3,1,1,4]
        # 4: GOOD
        # 1: GOOD
        # 1: GOOD
        # 3: GOOD
        # 2: GOOD 
        
        dp = [False for _ in range(len(nums))]
        
        for i in range(len(nums)):
            idx = len(nums) - i - 1
            if (idx + nums[idx] >= len(nums)-1) or True in dp[idx:idx+nums[idx]+1]:
                dp[idx] = True
        return dp[0]
        
        
        
        
