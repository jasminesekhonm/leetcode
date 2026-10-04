class Solution:
    def rob(self, nums: list[int]) -> int:

        def helper(arr):
            n = len(arr)

            if n == 0:
                return 0 
            
            if n == 1:
                return arr[0]

            if n == 2:
                return max(arr)

            dp = [0 for _ in range(n)]

            dp[0] = arr[0]
            dp[1] = arr[1]
            dp[2] = dp[0] + arr[2]
            
            for i in range(3, n):
                dp[i] = arr[i] + max(dp[i-2], dp[i-3])

            return max(dp)

        if len(nums) == 0:
            return 0 
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:-1]))
        

        
