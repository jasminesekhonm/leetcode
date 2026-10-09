class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        candidates.sort() # O(nlogn)

        candidates = [c for c in candidates if c <= target] # O(n)
        
        if len(candidates) == 0:
            return []

        res = [] # O(n)

        def helper(candidates, curr_sum, curr_comb):
            if curr_sum == target:
                res.append(curr_comb)

            for i, candidate in enumerate(candidates):
                if (target - curr_sum - candidate) < 0:
                    break
                helper(candidates[i:],curr_sum+candidate, curr_comb+[candidate])

        
        helper(candidates, 0, [])

        return res
