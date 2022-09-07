class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # [-2,1,-3,4,-1,2,1,-5,4]
        currentSubarray = maxSubarray = nums[0]
        for num in nums[1:]:
            currentSubarray = max(currentSubarray + num, num) 
            maxSubarray = max(currentSubarray, maxSubarray)
        return maxSubarray
        
        
