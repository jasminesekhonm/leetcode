from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = Counter(t)

        if len(t) > len(s):
            return ""
    
        ans = None
        i, j = 0, 0
        missing = len(t)
        while j < len(s) and missing > 0:
            char = s[j]
            if char in freq_t:
                if freq_t[char] > 0:
                    missing -= 1
                freq_t[char] -= 1
            j += 1
            while i <= j and missing == 0:
                if ans is None or j-i < len(ans):
                    ans = s[i:j]
                char = s[i]
                if s[i] in freq_t:
                    freq_t[char] += 1
                    if freq_t[char] > 0:
                        missing += 1

                i += 1
            
        return ans if ans is not None else ""

