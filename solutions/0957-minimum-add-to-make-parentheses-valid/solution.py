class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        n_open = 0
        n_invalid = 0
        for i, char in enumerate(s):
            if char == "(":
                n_open += 1
            else:
                if n_open > 0:
                    n_open -= 1
                else:
                    n_invalid += 1
                    n_open = 0
        
        return n_invalid + n_open

                
            
        
        
        
