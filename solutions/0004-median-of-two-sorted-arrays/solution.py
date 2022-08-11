class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0 
        j = 0 
        
        m, n = len(nums1), len(nums2)
        mn = m + n 
        
        res = []
        
        while i < m or j < n:
            if j >= n:
                res.append(nums1[i])
                i += 1
            elif i >= m:
                res.append(nums2[j])
                j += 1
            else:
                num1 = nums1[i]
                num2 = nums2[j]
                if num1 <= num2:
                    res.append(num1)
                    i += 1 
                elif num1 > num2:
                    res.append(num2)
                    j += 1
                
        # [0, 1, 2, 3] 
        ix = mn // 2
        if mn % 2 == 0:
            median = (res[ix-1] + res[ix]) / 2
        else:
            median = res[ix] 
        return median
            
        
        
        
            
                
        
