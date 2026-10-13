class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        res = []

        candidates.sort()

        candidates = [c for c in candidates if c <= target]
        
        n = len(candidates)

        def helper(start_index, remaining_target, current_combination):
            if remaining_target == 0:
                res.append(current_combination)

            if start_index >= n:
                return 
            
            if remaining_target < candidates[start_index]:
                return 

            for i in range(start_index, n):
                if i > start_index and candidates[i] == candidates[i-1]:
                    continue

                candidate = candidates[i]
                if candidate > remaining_target:
                    break 
                helper(i+1, remaining_target-candidate, current_combination + [candidate])

        
        helper(0, target, [])
        return res 
            
