class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ### are all the strings non-empty, have finite length?
        i = 0
        j = 0 
        res = "" 
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                res += word1[i]
            if j < len(word2):
                res += word2[j]
            i += 1
            j += 1
        return res 

        ### time complexity would be O(m+n)
        ### space complexity would be O(m+n)
        
