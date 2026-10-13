class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        nums = [num**2 for num in nums]

        n = len(nums)

        nums.sort() 

        return sum(nums[n//2:]) - sum(nums[:n//2])
       



