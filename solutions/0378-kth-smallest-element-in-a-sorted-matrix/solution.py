class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        i, j = 0, 0
        m, n = len(matrix), len(matrix[0])
        
        output = []
        
        
        for i in range(min(m, k)):
            output.append((matrix[i][0], i, 0))
            
        heapq.heapify(output)
        while k:
            (currMin, minRow, minCol) = heapq.heappop(output)
            if minCol < n - 1:
                heapq.heappush(output, (matrix[minRow][minCol+1], minRow, minCol+1))
            k -= 1
        return currMin
            
            
            
                
            
            
            
            
        
