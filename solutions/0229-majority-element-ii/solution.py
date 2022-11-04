class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqDict = Counter(nums)
        n = len(nums)
        return [k for k in freqDict if freqDict[k] > (n / 3)]
        
