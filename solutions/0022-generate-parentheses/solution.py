class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        o = '('
        c = ')'
        
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append(''.join(A))
            else:
                A.append(o)
                generate(A)
                A.pop()
                A.append(c)
                generate(A)
                A.pop()
        
        def valid(A):
            bal = 0 
            for c in A:
                if c == o: 
                    bal += 1
                else: 
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0
                
        ans = []
        generate()
        return ans
