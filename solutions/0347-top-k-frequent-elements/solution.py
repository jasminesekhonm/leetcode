class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqDict = defaultdict(int)
        
        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1 
        
        freqDict = sorted(freqDict.items(), key = lambda x: x[1])[::-1]
        return [k for (k, v) in freqDict[:k]]
        
        
        
