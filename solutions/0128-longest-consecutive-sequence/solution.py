class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1

        numSet = set(nums)

        best = 0

        for x in numSet:
            if x-1 not in numSet:
                length = 1
                while x+length in numSet:
                    length += 1
                best = max(best, length)

        return best 
