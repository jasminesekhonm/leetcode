class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqDict = defaultdict(int)
        
        for num in nums: 
            freqDict[num] = freqDict.get(num, 0) + 1

        return [k for (k, v) in freqDict.items() if v > (len(nums)//3)]
