class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # [1, 2, 2, 0, 0, 0]
        # [2, 5, 6]
        # ?3
        ptr1 = m-1
        ptr2 = n-1
        ptr3 = m+n-1
        
        while ptr2 >= 0:
            
            if nums2[ptr2] > nums1[ptr1] or ptr1 < 0:
                    nums1[ptr3] = nums2[ptr2]
                    ptr2 -= 1
                    
            elif nums1[ptr1] >= nums2[ptr2] or ptr2 < 0:
                    nums1[ptr3] = nums1[ptr1]
                    ptr1 -= 1
            ptr3 -= 1
                
        
        
