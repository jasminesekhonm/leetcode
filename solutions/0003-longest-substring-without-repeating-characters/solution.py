class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)

        if n <= 1:
            return n

        i, j = 0, 0

        max_len = 0

        char_set = set()

        while j < n: 
            while j < n and s[j] not in char_set:
                char_set.add(s[j])
                j += 1
            max_len = max(max_len, j-i)
            while j < n and s[j] in char_set:
                char_set.remove(s[i])
                i += 1
        
        
        return max_len
            

            
                




        
