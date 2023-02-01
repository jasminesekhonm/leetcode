class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                if matrix[i][0] == target or matrix[i][-1] == target:
                    return True 
                # binary search through row 
                l, r = 0, len(matrix[0])-1
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[i][mid] == target:
                        return True 
                    if matrix[i][mid] > target:
                        r = mid - 1
                    elif matrix[i][mid] < target:
                        l = mid + 1 
                return False 
        return False 

                
