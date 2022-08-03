class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) == 0:
            return True 
        if len(moves) == 1:
            return False 
        
        x, y = 0, 0
        for move in moves:
            if move == 'U':
                x, y = x, y + 1
            elif move == 'D':
                x, y = x, y - 1
            elif move == 'R':
                x, y = x + 1, y
            elif move == 'L':
                x, y = x - 1, y
        return (x, y) == (0, 0)
        
