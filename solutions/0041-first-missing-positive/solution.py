class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minValue = 1 
        maxValue = max(nums)
        if maxValue <= 0:
            return 1 
        freqCounter = Counter(nums)
        for num in range(minValue, maxValue+1):
            if num not in freqCounter:
                return num
        return maxValue+1
