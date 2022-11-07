class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freqDict = defaultdict(int)
        
        for num in range(1, len(nums)+1):
            freqDict[num] = 0 

        for num in nums:
            freqDict[num] += 1

        missingNumber = [k for k in freqDict if freqDict[k] == 0][0]
        duplicateNumber = [k for k in freqDict if freqDict[k] > 1][0]

        return [duplicateNumber, missingNumber]
