class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []

        for num in range(n+1):
            ret, power = 0, 31 
            while power >= 0:
                ret += (num & 1)
                num = num >> 1 
                power -= 1
            res.append(ret)
        return res 

        
