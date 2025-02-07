class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [0, 1, 0, 3, 12]
        # [1, 0, 0, 3, 12]
        # [1, 0, 0, 3, 12]
        # [1, 3, 0, 0, 12]
        # [1, 3, 12, 0, 0]

        pos = 0
        for i in range(len(nums)):
            el = nums[i]
            if el != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
                

