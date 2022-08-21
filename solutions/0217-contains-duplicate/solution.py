class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freqDict = collections.Counter(nums)
        return max(freqDict.values()) > 1
        
