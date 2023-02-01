class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        

        q = deque()
        
        for candidate in candidates:
            q.append(([candidate], candidate))

        res = []
        
        while q:
            
            currComb, currSum = q.pop()
            if currSum == target and sorted(currComb) not in res:
                res.append(sorted(currComb))

            for candidate in candidates:
                if (currSum + candidate) <= target and candidate >= currComb[-1]:
                    q.append((currComb + [candidate], currSum + candidate))

        return res 

        
        

