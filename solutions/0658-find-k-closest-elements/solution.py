class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # sorted integer array
        # return k closest elements to x
        # [1,2,3,4,5]
        # [-3, -2, -1, 0, 1, 2, 3]
        # [2, 1, 1, 2, 3] # rotated array 
        # -1
        # [2, 3, 4, 5, 6]
        left = 0
        right = len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left+k]
                
            
