class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        ans = 0 

        def expand_palindrome(i, j):
            nonlocal ans
            while i >= 0 and j < n and s[i] == s[j]:
                ans += 1
                i -= 1
                j += 1
            
        
        for i in range(n):
            expand_palindrome(i, i)
            if i < n-1:
                expand_palindrome(i, i+1)

        return ans
        
