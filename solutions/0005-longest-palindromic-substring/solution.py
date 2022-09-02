class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) == 0:
            return " "
        
        if len(s) == 1 or (len(s) == 2 and s[0] == s[1]):
            return s 
        
        elif len(s) == 2 and s[0] != s[1]:
            return s[0]
    
        start, end = 0, 0
        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i + 1)
            bestLen = max(len1, len2)
            if (bestLen > end - start):
                start = i - (bestLen - 1) // 2
                end = i + bestLen // 2 
        return s[start:end+1]
    
def expandAroundCenter(s, left, right):
    l, r = left, right 
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1 

                
        
