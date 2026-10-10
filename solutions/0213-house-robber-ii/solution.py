class Solution:
    def rob(self, nums: list[int]) -> int:
        
        def base_case(houses):
            n = len(houses)

            if n == 0:
                return 0
            
            if n == 1:
                return houses[0]

            dp = [0] * n 

            dp[0] = houses[0]
            dp[1] = houses[1]
            
            if n == 2:
                return max(dp)

            dp[2] = houses[2] + houses[0]

            for i in range(3,n):
                dp[i] = houses[i] + max(dp[i-2], dp[i-3])

            return max(dp)

        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
            
        return max(base_case(nums[1:]), base_case(nums[:-1]))

