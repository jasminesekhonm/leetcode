class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        subsets = []
        candidates.sort()
        
        for idx, candidate in enumerate(candidates):
            left = target - candidate
            if left == 0:
                subsets.append([candidate])
            elif left > 0:
                for subset in self.combinationSum(candidates[idx:], left):
                    subsets.append([candidate] + subset)
        return subsets
