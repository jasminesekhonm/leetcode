class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        val_set = set()

        for num in nums:
            if num in val_set:
                return True
            val_set.add(num)
        
        return False
