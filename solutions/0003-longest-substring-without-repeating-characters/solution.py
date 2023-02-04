class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0 
        uniqueChars = set()
        maxLen = 0 

        while l <=r and r < len(s):
            if s[r] not in uniqueChars:
                uniqueChars.add(s[r])
                maxLen = max(maxLen, r - l + 1)
                r += 1
            else:
                while s[r] in uniqueChars:
                    uniqueChars.remove(s[l])
                    l += 1 
                maxLen = max(maxLen, r - l + 1)
            
        
        return maxLen 
