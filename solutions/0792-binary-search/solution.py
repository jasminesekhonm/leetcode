class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binarySearch(left, right):
            if left < 0 or right > len(nums)-1 or left > right:
                return -1 
            mid = (left + right) // 2
            if target == nums[mid]:
                res = mid
            elif target > nums[mid]:
                left = mid+1
                res = binarySearch(left, right)
            elif target < nums[mid]:
                right=mid-1
                res = binarySearch(left, right)
            return res 
        return binarySearch(0, len(nums)-1)
        
                
