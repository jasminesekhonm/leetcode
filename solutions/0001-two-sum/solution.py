class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    ## what are my assumptions?
    ### can I assume that the answer always exists
    ### there is only one solution 
    ### can be negatives

        complements = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complements:
                return [i, complements[complement]]
            complements[nums[i]] = i 
        return []
        
