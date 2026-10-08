from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)

        if n <= 1:
            return n
        
        # freq = defaultdict(int)
        # for char in s:
        #     freq[char] += 1
        
        # if max(freq.values()) == 1:
        #     return n
        
        l = r = 0

        max_len = 0
        curr_substring = set()
        # two pointer approach
        # start with the smallest string , e.g. a
        # and keep increasing length until i hit
        # a duplicate character

        while r < n:

            while r < n and s[r] not in curr_substring:
                curr_substring.add(s[r])
                max_len = max(max_len, r - l + 1)
                r += 1
            while r < n and s[r] in curr_substring:
                curr_substring.remove(s[l])
                l += 1
        
        return max_len
            


        # maintain a set of curr string char values
        # or a freq dict

        # once i hit a duplicate character, increase
        # start point until freq == 1

