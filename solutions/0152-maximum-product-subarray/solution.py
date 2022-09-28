class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # [-2, 0, -1]
        # -2
        # -2 * 0 >= 0 > -2
        # -2 * 0 >=
        
        maxCurr = nums[0]
        minCurr = nums[0]
        result = maxCurr
        
        for i in range(1, len(nums)):
            curr = nums[i]
            tempMax = max(curr, maxCurr * curr, minCurr * curr)
            minCurr = min(curr, minCurr * curr, maxCurr * curr)
            maxCurr = tempMax
            result = max(maxCurr, result)
        return result
                
