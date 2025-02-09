from collections import defaultdict 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        numDict = defaultdict(int)
        for num in nums:
            numDict[num] += 1
        
        for num in numDict:
            if numDict[num] == 1:
                return num

        


