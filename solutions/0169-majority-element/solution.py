class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freqDict = defaultdict(int)
        for num in nums:
            freqDict[num] = freqDict.get(num, 0) + 1
            if freqDict[num] > len(nums) // 2:
                return num 
