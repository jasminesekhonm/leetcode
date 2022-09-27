class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(arr):
            left, right = 0, len(arr)-1
            while left <= right and right < len(arr):
                mid = (left + right) // 2
                if target == arr[mid]:
                    return True 
                if target < arr[mid]:
                    right = mid - 1
                elif target > arr[mid]:
                    left = mid + 1
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        
        row, col = 0, 0
        
        while row < rows:
            if target >= matrix[row][0] and target <= matrix[row][-1]:
                return binarySearch(matrix[row])
            row = row + 1
        return False
                
                
