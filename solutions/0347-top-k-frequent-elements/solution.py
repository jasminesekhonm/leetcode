class Solution:
    def topKFrequent(self, nums: List[int], val: int) -> List[int]:
        freqDict = Counter(nums)
        res = [k for k, v in sorted(freqDict.items(), key = lambda x: x[1])][-val:]
        return res
        
        
        
