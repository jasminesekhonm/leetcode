class Solution:
    def hammingWeight(self, n: int) -> int:
        a=bin(n)[2:]
        a=a.replace("0","")
        return len(a)
        
