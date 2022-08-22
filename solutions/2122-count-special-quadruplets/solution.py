class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[j] + nums[k] + nums[i] in nums[k:]:
                        count += nums[k:].count(nums[j] + nums[k] + nums[i])
                        
        return count
