class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqDict = Counter(nums)
        freqDict = sorted(freqDict.items(), key = lambda x: x[1])

        topFreq = [k for (k, v) in freqDict[-k:]]
        return topFreq
