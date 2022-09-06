class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        indexedArr = [[v, i] for i, v in enumerate(arr)]
        sortedArr = sorted(indexedArr, key = lambda x: x[0])
        return sortedArr[-1][1]
        
