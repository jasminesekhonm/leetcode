class Solution:
    def check_palindrome(self,string):
        return string == string[::-1]
    
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        combined_string = a + b
        if a == a[::-1] or b == b[::-1] or combined_string == combined_string[::-1]:
            return True 
        
        return self.solve(a, b) or self.solve(b, a)
        
    def solve(self, a, b):
        
        i = 0
        j = len(a) - 1
        while i < j and a[i] == b[j]:
            i += 1
            j -= 1
        
        return self.check_palindrome(a[:i] + b[i:]) or self.check_palindrome(a[:j+1] + b[j+1:])
            
        
        
