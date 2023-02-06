class Solution:
    def canJump(self, nums: List[int]) -> bool:

        dp = [False for _ in range(len(nums))]

        dp[-1] = True 

        for i in range(len(nums)-2,-1,-1):
            print(i)
            maxJump = nums[i]
            j = min(i+maxJump, len(nums)-1)
            print(j)
            while j > i and not dp[j]:
                j -= 1 
            dp[i] = True if dp[j] else False 

        
                
            




        return dp[0]
            

