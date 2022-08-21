class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rowDict = defaultdict(list)
        colDict = defaultdict(list)
        boxDict = defaultdict(list)
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                rowDict[i] = []
                colDict[j] = []
                boxDict[(i//3, j // 3)] = []
                
        
        
        for i in range(m):
            for j in range(n):
                elem = board[i][j]
                
                if elem.isdigit(): 
                    elem = int(elem)
                
                    if not (0 < elem < 10) or (elem in rowDict[i]) or (elem in colDict[j]) or (elem in boxDict[(i//3, j//3)]):
                        return False 
               
                    rowDict[i].append(elem)
                    colDict[j].append(elem)
                    boxDict[(i//3, j//3)].append(elem)
        return True
                    
                
        
        
