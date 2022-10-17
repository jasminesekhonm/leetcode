class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        freqDict = defaultdict(int)
        for char in sentence:
            if char.isalpha():
                freqDict[char] = freqDict.get(char, 0) + 1
        return len(freqDict) == 26 and min(freqDict.values()) >= 1
        
