class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mapNums = {}
        for num in nums:
            if num in mapNums:
                mapNums[num] += 1
            else:
                mapNums[num] = 1
        return [k for k, v in mapNums.items() if v == 2]
        
