class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()

        combinations = set()

        def twoSum(num, index, target):
            complements = set()
            two_sum_combinations = []
            j = index 
            while j < n:
                candidate = nums[j]
                complement = target - candidate 
                if complement in complements:
                    combinations.add((num, target-candidate, candidate  ))
                    while j + 1 < n and nums[j+1] == nums[j]:
                        j += 1 
                complements.add(candidate)
                j += 1
            
    


        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            num = nums[i]
            remaining = -num

            twoSum(num, i+1, remaining)

            

        return list(combinations)

        
