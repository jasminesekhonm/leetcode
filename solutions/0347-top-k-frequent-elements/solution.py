class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        frequency_dict = {}

        for num in nums:
            frequency_dict[num] = frequency_dict.get(num, 0) + 1

        buckets = [[] for _ in range(n+1)]

        for num in frequency_dict:
            buckets[frequency_dict[num]].append(num)


        res = []

        for i in range(n, 0, -1):

            bucket = buckets[i]
            if len(bucket) > 0:
                res = res + bucket
                if len(res) == k:
                    return res
        return res     


        
        
