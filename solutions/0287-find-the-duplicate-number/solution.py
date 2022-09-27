class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freqDict = Counter(nums)
        return [k for k in freqDict if freqDict[k] > 1][0]
        
