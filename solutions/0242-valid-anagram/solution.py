from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) > len(s):
            s, t = t, s
        freq = Counter(s)
        for char in t:
            if char not in freq:
                return False
            freq[char] -= 1

        return max(freq.values()) == 0 
        
