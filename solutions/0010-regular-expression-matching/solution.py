class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dp = {}

        def helper(i, j):
            if (i, j) not in dp:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], "."}
                    if j + 1 < len(p) and p[j + 1] == "*":
                        ans = helper(i, j+2) or first_match and helper(i+1, j)
                    else:
                        ans = first_match and helper(i + 1, j + 1)
                    
                
                dp[i, j] = ans 
            
            return dp[i, j]

        return helper(0, 0)
