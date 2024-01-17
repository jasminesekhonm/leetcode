class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqDict = defaultdict(int)
        for val in arr:
            freqDict[val] = freqDict.get(val, 0) + 1 
        
        return len(set(freqDict.values())) == len(freqDict.values())

        
