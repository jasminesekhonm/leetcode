class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def expand(i, j):
            num_palindromes = 0
            while i >= 0 and j < n and s[i] == s[j]:
                num_palindromes += 1
                i -= 1
                j += 1
            return num_palindromes
        
        ans = sum([expand(i, i) + expand(i, i+1) for i in range(n)])
        return ans

