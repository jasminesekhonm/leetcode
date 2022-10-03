class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        seen = set()
        maxSubsets = pow(2, n)
        
        res = []
        
        for subsetIndx in range(maxSubsets):
            currentSubset = []
            hashcode = ''
            for j in range(n):
                mask = 1 << j 
                isSet = mask & subsetIndx 
                if isSet:
                    currentSubset.append(nums[j])
                    hashcode += str(nums[j]) + ','
                if hashcode not in seen:
                    seen.add(hashcode)
                    res.append(currentSubset)
        return res
            
            
        
