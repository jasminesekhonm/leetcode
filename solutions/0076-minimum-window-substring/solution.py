class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return "" 

        def isequal(currentDict, tDict):
            for k, v in tDict.items():
                if k not in currentDict or currentDict[k] < tDict[k]:
                    return False 
            return True 

        tDict = Counter(t)
        l, r = 0, 0 
        ans = [float('inf'), None, None]

        currentDict = defaultdict(int)
        formed = 0 

        maxWindow = float('inf')
        currWindow = 0 

        while l <= r and r < len(s):
            newChar = s[r]
            currentDict[newChar] = currentDict.get(newChar, 0) + 1
            
            while isequal(currentDict, tDict) and l <= r:
                currWindow = r - l + 1 
                maxWindow = min(currWindow, maxWindow)
                if maxWindow == currWindow:
                    ans = [maxWindow, l, r]
                lastChar = s[l]
                currentDict[lastChar] -= 1 
                l += 1 
            
            

            r += 1 
        
        return s[ans[1]:ans[2]+1] if ans[1] is not None else ""


                

            
        
