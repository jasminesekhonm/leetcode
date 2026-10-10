from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        freq = defaultdict(int)
        n = len(nums)

        for num in nums:
            freq[num] += 1
        
        min_heap = [(-freq[num], num) for num in freq]
        heapq.heapify(min_heap)

        res = []
        for i in range(k):
            _, num = heapq.heappop(min_heap)
            res.append(num)

        return res


        
