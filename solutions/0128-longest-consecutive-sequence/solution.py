class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        if len(nums) == 1:
            return 1
        n = len(nums)
        num_set = set(nums)
        max_streak = 1
        for num in num_set:
            if num - 1 not in num_set:
                current_streak = 1
                current_num = num 
                while current_num + 1 in num_set:
                    current_streak += 1 
                    current_num += 1 
                max_streak = max(current_streak, max_streak)
        
        return max_streak 
                
        
        
