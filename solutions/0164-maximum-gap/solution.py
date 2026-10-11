class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)

        min_num = min(nums)
        max_num = max(nums)

        if min_num == max_num:
            return 0 

        gap = (max_num - min_num) // n + 1

        n_buckets = (max_num - min_num) // gap + 1

        buckets = [(None, None) for _ in range(n_buckets)]

        for num in nums:
            bucket_index = (num - min_num) // gap 
            
            min_bucket, max_bucket = buckets[bucket_index]
            if min_bucket is None:
                min_bucket = max_bucket = num 
            else:
                min_bucket = min(min_bucket, num)
                max_bucket = max(max_bucket, num)
            buckets[bucket_index] = (min_bucket, max_bucket)
        
        best_gap = 0
        prev_max = min_num
        for (new_min, new_max) in buckets:
            if not new_min is None:
                best_gap = max(best_gap, new_min - prev_max)
                prev_max = new_max 

        return best_gap
