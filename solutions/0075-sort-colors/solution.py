class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # [2, 0, 2, 1, 1, 0]

        n = len(nums)
        
        swap = True 

        while swap:
            swap = False 

            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    swap = True

            
