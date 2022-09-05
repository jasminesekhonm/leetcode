class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        arrStart, arrEnd = 0, 0
        freqDict = defaultdict(int)
        freqDict[s[0]] = 1
        lenSubstring=1
        while arrStart <= arrEnd and arrEnd < len(s)-1:
            arrEnd += 1
            freqDict[s[arrEnd]] += 1
            while max(freqDict.values()) > 1:
                freqDict[s[arrStart]] -= 1
                arrStart += 1
            lenSubstring = max(lenSubstring, arrEnd-arrStart+1)
        return lenSubstring
