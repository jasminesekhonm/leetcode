class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(1)
        # O(n)
        complements = defaultdict(int)
        for i, num in enumerate(nums):
            if num in complements:
                return [i, complements[num]]
            else:
                complements[target - num] = i
        return -1  

