class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for j, num in enumerate(nums2):
            nums1[m + j] = num
            
        return nums1.sort()
            
