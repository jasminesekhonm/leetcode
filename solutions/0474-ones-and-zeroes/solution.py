class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        numZeroesDict = defaultdict(int)
        numOnesDict = defaultdict(int)
        for i, string in enumerate(strs):
            numZeroesDict[i] = sum([1 for char in string if char=='0'])
            numOnesDict[i] = sum([1 for char in string if char=='1'])
            
        if sum(numZeroesDict.values()) <= m and sum(numOnesDict.values()) <= n:
            return len(strs)
        
        q = []
        q.append(("", 0, 0, 0))
        
        resDict = {}
        
        while q:
            currIdx, currLen, currZeroes, currOnes = q.pop()
            
            for i in range(len(strs)):
                if not str(i) in currIdx.split(','):
                    numZeroes = currZeroes + numZeroesDict[i]
                    numOnes = currOnes + numOnesDict[i]
                    newLen = currLen + 1
                    if numZeroes <= m and numOnes <= n and ((numZeroes, numOnes) not in resDict or resDict[(numZeroes, numOnes)] < newLen):
                        resDict[(numZeroes, numOnes)] = newLen
                        q.append((currIdx + "," + str(i), newLen, numZeroes, numOnes))
                        
        return max(resDict.values()) if len(resDict) > 0 else 0
                        
        
                        
                    
                    
            
            
        
