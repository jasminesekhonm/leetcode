class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freqDict = defaultdict(int)
        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1
        return [k for k in freqDict if freqDict[k] == 1]
            
