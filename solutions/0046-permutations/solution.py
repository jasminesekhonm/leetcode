class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = []

        def backtrack(firstIdx):
            if firstIdx == n:
                res.append(nums[:])

            for j in range(firstIdx, n):
                nums[firstIdx], nums[j] = nums[j], nums[firstIdx]
                backtrack(firstIdx + 1)
                nums[firstIdx], nums[j] = nums[j], nums[firstIdx]
        
        backtrack(0)
        return res 

                
        
