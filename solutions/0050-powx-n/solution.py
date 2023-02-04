class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1 

        def power(x, n, ans):
            if n % 2 == 0:
                x = (x*x)
                n = n / 2 
                ans *= power(x, n)
            else:
                n = n - 1
                ans *= (x * power(x, n))
            return ans 

        return pow(x, n)
