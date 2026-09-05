class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumOfSquares(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        
        slow = n
        fast = n
        
        while True:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))
            
            if slow == fast:
                break
        
        return slow == 1
