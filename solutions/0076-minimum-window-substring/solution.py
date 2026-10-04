class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""
        
        if len(s) == len(t) and s == t:
            return s 
        

        t_dict = {}

        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        
        i, j = 0, 0 

        missing = len(t)
        best_len = float('inf')
        best_ix = (None, None)
        while j < len(s) and missing > 0:
            char = s[j]
            if char in t_dict:
                
                if t_dict[char] > 0:
                    missing -= 1 
                t_dict[char] -= 1
            j += 1 

            while  missing == 0:
                if (j - i) < best_len:
                    best_len = j - i 
                    best_ix = (i, j)
                char = s[i]
                if char in t_dict:
                    t_dict[char] += 1
                    if t_dict[char] > 0:
                        missing += 1
                i += 1

        i, j = best_ix 
        
        return "" if i is None else s[i:j]

            



         
        
        


        
        
