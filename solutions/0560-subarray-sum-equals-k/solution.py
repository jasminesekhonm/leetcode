class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, currSum = 0, 0 

        sumDict = {}
        sumDict[0] = 1

        for i in range(len(nums)):
            currSum += nums[i]
            if (currSum - k) in sumDict:
                count += sumDict[currSum-k]
            if currSum in sumDict:
                sumDict[currSum] = sumDict[currSum] + 1
            else:
                sumDict[currSum] = 1 
        
        return count
