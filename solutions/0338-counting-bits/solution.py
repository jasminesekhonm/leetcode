class Solution:
    def countBits(self, n: int) -> list[int]:
        
        if n == 0:
            return [0]
        
        ans = [0] * (n + 1)

        for x in range(1, n+1):
            ans[x] = ans[x >> 1] + (x & 1)
        return ans 



