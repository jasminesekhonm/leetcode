from collections import Counter 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = "abcabcbb"

        i, j = 0, 0 
        
        charSet = set()

        maxLength = 0 

        for j in range(len(s)):
            while s[j] in charSet:
                charSet.remove(s[i])
                i += 1 
            charSet.add(s[j])
            maxLength = max(maxLength, j - i + 1)

        return maxLength
            
            
        
