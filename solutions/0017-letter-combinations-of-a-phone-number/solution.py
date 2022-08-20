class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
        
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        if len(digits) == 1:
            return list(letters[digits])
        
        
        output = []
        
        # 235
        # ad, ae, af, bd, be, bf, cd, ce, cf
        # 5
        # adj, aej, afj, bdj, bfj, cdj, cfg, cej, ..., cfl 
        # 6
        
        def findCombinations(combList, currDigit):
            return [''.join((string, char)) for string in combList for char in letters[currDigit]]
            
        
        
        
        
        digit1 = digits[0]
        digit2 = digits[1]
        combinations = [''.join((char1, char2)) for char1 in letters[digit1] for char2 in letters[digit2]]
        
        for ix in range(2, len(digits)):
            combinations = findCombinations(combinations, digits[ix])
        
        return combinations
            
            
            
        
        
            
        
        
            
                    
            
        
        
        
        
            
            
        
        
        
        
