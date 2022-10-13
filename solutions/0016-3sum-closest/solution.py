class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() # O(nlogn)
        diff = float('inf')
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sumval = nums[i] + nums[lo] + nums[hi]
                if abs(target-sumval) < abs(diff):
                    diff = target - sumval 
                if sumval < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break 
        return target - diff
