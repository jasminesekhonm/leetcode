class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resultDict = {}

        for i in range(len(nums)):
            num = nums[i]
            # print(num, target-num, resultDict)
            if target - num in resultDict:
                return [resultDict[target-num], i]
            resultDict[num] = i

        return []
