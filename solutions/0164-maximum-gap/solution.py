class Solution:
    def maximumGap(self, nums: list[int]) -> int:

        n = len(nums)
        if n < 2:
            return 0 

        max_num = min_num = nums[0]

        for num in nums[1:]:
            max_num = max(max_num, num)
            min_num = min(min_num, num)

        
        gap = max(1, (max_num - min_num) // (n - 1)) ## assume evenly spaced 

        n_buckets = (max_num - min_num) // gap + 1 

        buckets = [[None, None] for _ in range(n_buckets)]

        for num in nums:
            index = (num - min_num) // gap 

            if buckets[index][0] is None:
                buckets[index][0] = buckets[index][1] = num 
            
            else:
                buckets[index][0] = min(buckets[index][0], num)
                buckets[index][1] = max(buckets[index][1], num)

        prev_max = min_num 
        max_diff = 0 
        for i in range(n_buckets):
            if buckets[i][0] is None:
                continue  
            diff = buckets[i][0] - prev_max 
            max_diff = max(diff, max_diff)

            prev_max = buckets[i][1]

        return max_diff

        
