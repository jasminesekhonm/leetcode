class Solution:
    def maxLength(self, arr: List[str]) -> int:

        q = []
        
        for i, word in enumerate(arr):
            if len(word) == len(set(word)):
                q.append((word, i, len(word)))

        maxLen = 0 
        while q:
            currWord, currIdx, currLen = q.pop()

            maxLen = max(maxLen, currLen)

            for j in range(currIdx+1, len(arr)):
                newWord = currWord + arr[j]
                if len(newWord) == len(set(newWord)):
                    q.append((newWord, j, len(newWord)))

            
        return maxLen 

        




        
