class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        # is it only integers, can they be negative, is it sorted 

        # store the length of the consecutive element sequence starting at that element 
     
        bestLength = 0
        numSet = set(nums)
        for num in numSet:
            if (num-1) not in numSet:
                 
                maxLength = 1
                while (num+1 in numSet):
                    num += 1
                    maxLength += 1
                    
                bestLength = max(maxLength, bestLength)
            
        return bestLength

            

