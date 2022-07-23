class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return nums 
        if len(nums) == 2:
            if sum(nums) == target:
                return [0, 1]
            return []
        
        for i in range(len(nums)):
            first_elem = nums[i]
            required_elem = target - first_elem
            for j in range(i + 1, len(nums)):
                if nums[j] == required_elem:
                    return [i, j]
                
        return []
        
