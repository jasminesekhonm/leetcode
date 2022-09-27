class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counterDict = Counter(nums)
        counterDict = sorted(list(counterDict.items()), key = lambda x: x[1])[::-1]
        return [key for key, v in counterDict[:k]]
