class Solution:
    def minimumSum(self, num: int) -> int:
        
        digits = []
        while num:
            digit, num = num % 10, num // 10
            digits.append(digit)
            
        digits = sorted(digits)
        lenNew = 2 
        
        new1 = 10 * digits[0] + digits[2]
        new2 = 10 * digits[1] + digits[3]
        
        return new1 + new2
        
