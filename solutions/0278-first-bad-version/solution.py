# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n 
        while left <= right:
            mid = (left + right) // 2 
            if not isBadVersion(mid-1) and isBadVersion(mid):
                return mid
            elif isBadVersion(mid): # check if it is first one
                right = mid - 1 
            else:
                left = mid + 1
                
                
        
