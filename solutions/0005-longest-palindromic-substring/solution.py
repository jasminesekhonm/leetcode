class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand_around_center(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]

        max_len = 0
        res = ""
        for i in range(len(s)):
            res1 = expand_around_center(i, i)
            res2 = expand_around_center(i, i+1)
            if len(res1) >= len(res2) and len(res1) >= max_len:
                max_len = len(res1)
                res = res1
            elif len(res2) > len(res1) and len(res2) >= max_len:
                max_len = len(res2)
                res = res2

        return res


        

        
