class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freqCount = defaultdict(int)
        for num in nums:
            freqCount[num] = freqCount.get(num, 0) + 1
        
        return [num for num in freqCount if freqCount[num] == 1][0]
            
        
