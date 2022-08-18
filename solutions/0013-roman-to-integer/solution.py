class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
                        'C': 100, 'D': 500, 'M': 1000}
        
        total = 0
        i = 0
        n = len(s)
        while i < n:
            if i + 1 < len(s) and romanDict[s[i]] < romanDict[s[i+1]]:
                total += romanDict[s[i+1]] - romanDict[s[i]]
                i += 2
            else:
                total += romanDict[s[i]]
                i += 1
        return total
        
        
