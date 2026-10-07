class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join([char.lower() for char in s if char.isalnum()])

        i,j = 0, len(s)-1

        while i <= j and s[i] == s[j]:
            i += 1
            j -= 1

        return (i >= j)
        
