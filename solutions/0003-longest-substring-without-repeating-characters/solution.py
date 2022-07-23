class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       # "abcbca"
    
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        maxLen = 0
        
        for i in range(len(s)):
            unique_chars = []
            for j in range(len(s)-i):
                elem = s[i+j]
                if ord(elem) not in unique_chars:
                    unique_chars.append(ord(elem))
                    maxLen = max(maxLen, len(unique_chars))
                    
                else:
                    break
        return maxLen
                
       
        
        
                
