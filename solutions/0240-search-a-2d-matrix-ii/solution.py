class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # relevant rows are rows where the first element is less than the target
        myHeap = []
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            if matrix[i][0] <= target <= matrix[i][-1]:
                myHeap.append((matrix[i][0], i, 0))
                
        heapq.heapify(myHeap)
        while len(myHeap) > 0:
            currElem, currRow, currCol = heapq.heappop(myHeap)
            if currElem == target:
                return True
            
            if currCol + 1 < cols and target >= matrix[currRow][currCol + 1]:
                heapq.heappush(myHeap, (matrix[currRow][currCol+1], currRow, currCol+1))
        return False
            
