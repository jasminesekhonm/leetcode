class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        combinations = []
        candidates.sort()
        candidates = [c for c in candidates if c <= target]
        if len(candidates) == 0:
            return []
        
        def helper(candidates, target, combination):
            if target == 0:
                combinations.append(combination)
                return 
            for i, candidate in enumerate(candidates):
                if candidate > target:
                    continue 
                helper(candidates[i:], target-candidate, combination + [candidate])
        
        helper(candidates, target, [])
        return combinations 
        
