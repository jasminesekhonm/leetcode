class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # choose each character as the target 

        # start from left and extend until char + others fit criteria
        # once it exceeds k, start moving left index 

        best = 0

        for target in set(s):
            l = others = 0

            for r, ch in enumerate(s):
                others += ch != target 

                while others > k:
                    others -= s[l] != target
                    l += 1
                
                best = max(best, r-l+1)
        
        return best
