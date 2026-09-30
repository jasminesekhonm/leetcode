class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # are they always integers
        # can they be negative
        # is the list sorted
        # can two duplicate numbers exist
        # can I use the same index twice 

        # brute force would be to loop over all pairs of numbers 
        # time complexity for that would be O(n^2)

        complementsDict = {}

        # [2, 7, 11, 15]
        # 2: 0 
        # 7: 1, [1, 0 ]
        for i, num in enumerate(nums):
            if (target-num) in complementsDict:
                return [i, complementsDict[target-num]]
            complementsDict[num] = i 
            
        return [-1, -1]
