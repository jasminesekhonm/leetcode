class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        string_ = [char.lower() for char in s if char.isalnum()]
        
        return string_ == string_[::-1]
        
