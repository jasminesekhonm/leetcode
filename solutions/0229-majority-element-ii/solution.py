from collections import defaultdict

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        
        n = len(nums)

        if n <= 1:
            return nums 

        
        freq_dict = defaultdict(int)

        for num in nums: # O(n)
            freq_dict[num] += 1

        ans = []
        for num in freq_dict: # O(n)
            if freq_dict[num] > n // 3:
                ans.append(num)
                if len(ans) == 2:
                    return ans 

        
        return ans
        

