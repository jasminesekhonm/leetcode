class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqDict = {}
        for char in s:
            if char not in freqDict:
                freqDict[char] = 0
            freqDict[char] += 1

        for char in t:
            if char not in freqDict:
                return False
            freqDict[char] -= 1
            if freqDict[char] < 0:
                return False
        
        return max(freqDict.values()) == 0
        
