class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        
        num_ones = s.count("1")
        
        if num_ones < k:
            return ""
        
        ans = s 
        left = cnt = 0 
        for right, ch in enumerate(s):
            cnt += int(ch)
            while cnt > k or s[left] == '0':
                cnt -= int(s[left])
                left += 1
            if cnt == k:
                t = s[left:right+1]
                if len(t) < len(ans) or len(t) == len(ans) and t < ans:
                    ans = t

                
        return ans
        
