class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        
        res = [[1], [1, 1]]
        if numRows == 2:
            return res 

        for row in range(3, numRows+1):
            prevRow = res[-1]
            currRow = [1 for _ in range(row)]
            for col in range(1, len(currRow)-1):
                currRow[col] = prevRow[col-1] + prevRow[col]
            res.append(currRow)
        
        return res 

        

        
