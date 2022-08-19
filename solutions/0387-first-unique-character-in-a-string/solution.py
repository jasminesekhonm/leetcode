class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        output = collections.Counter(s)
        
        for idx, ch in enumerate(s):
            if output[ch] == 1:
                return idx
        return -1
        
            
        
