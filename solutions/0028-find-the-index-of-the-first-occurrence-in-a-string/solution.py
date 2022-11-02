class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        startingPtrs = [i for i in range(len(haystack)) if haystack[i] == needle[0]]
        needleLen = len(needle)
        for ptr in startingPtrs:
            if ptr+needleLen <= len(haystack) and haystack[ptr:ptr+needleLen] == needle:
                return ptr
        return -1
                
            
        
