class Solution:
    def hammingWeight(self, n: int) -> int:
        ret, power = 0, 31 
        while power >= 0:
            ret += (n & 1)
            n = n >> 1
            power -= 1
        
        return ret 
        
