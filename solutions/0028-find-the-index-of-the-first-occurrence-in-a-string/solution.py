class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        indices = [i for i in range(len(haystack)) if haystack[i] == needle[0]]
        n = len(needle)
        for start_idx in indices:
            if haystack[start_idx:start_idx+n] == needle:
                return start_idx
        
        return -1
