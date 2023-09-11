class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = {0: [], 1: []}
        for num1 in nums1:
            if num1 not in nums2 and num1 not in res[0]:
                res[0].append(num1)
        
        for num2 in nums2:
            if num2 not in nums1 and num2 not in res[1]:
                res[1].append(num2)

        return res.values()
