class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        freqDictChars = Counter(chars)
        
        res = 0
        
        for word in words:
            freqDictWord = Counter(word)
            validWord = True
            for char in freqDictWord:
                if (char not in freqDictChars) or (char in freqDictChars and freqDictChars[char] < freqDictWord[char]):
                    validWord = False
                    break 
            if validWord:
                res += len(word)
        return res
                    
                
                
            
        
