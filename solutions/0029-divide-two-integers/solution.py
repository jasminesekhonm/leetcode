class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        q = 0
        dd, dv = abs(dividend), abs(divisor)
        
        while dd >= dv:
            powerOfTwo = 1
            value = dv 
            
            while (value + value < dd):
                value += value
                powerOfTwo += powerOfTwo
                
            q += powerOfTwo
            dd -= value 
        
        q = q if ((dividend >= 0 and divisor >= 0) or (dividend < 0 and divisor < 0)) else -q
        
        if q < -2**31:
            q = -2**31
        elif q >= 2**31:
            q = 2**31-1
        
        return q
