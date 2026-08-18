class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        countDict = {}

        if k == len(nums): ## only one subarray exists 
            return max(nums)
        
        for num in nums:
                if num in countDict:
                    countDict[num] += 1
                else:
                    countDict[num] = 1 

        if k == 1: ## all subarrays are length 1 
            oneCount = [k for k,v in countDict.items() if v == 1]
            return max(oneCount) if len(oneCount) != 0 else -1 
        
        else:
            maxEnd = max([nums[0], nums[-1]])
            minEnd = min([nums[0], nums[-1]])
            if countDict[maxEnd] == 1:
                return maxEnd
            elif countDict[minEnd] == 1:
                return minEnd
            return -1
        
            
        

        
