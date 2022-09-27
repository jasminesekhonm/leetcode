class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentArr = maxArr = nums[0]
        for num in nums[1:]:
            currentArr = max(currentArr + num, num)
            maxArr = max(currentArr, maxArr)
        return maxArr
