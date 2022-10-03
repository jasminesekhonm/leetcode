class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        else:
            numberToInsert = nums.pop()
            subPermutations = self.permute(nums)
            permutations = []
            for p in subPermutations:
                for i in range(0, len(p) + 1):
                    copied = p.copy()
                    copied.insert(i, numberToInsert)
                    permutations.append(copied)
        return permutations
