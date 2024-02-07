class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the occurence on each character
        cnt = collections.Counter(s)
        
        # Build heap
        heap = [(-v, k) for k, v in cnt.items()]
        heapq.heapify(heap)
        
        # Build string
        res = []
        while heap:
            v, k = heapq.heappop(heap)
            res += [k] * -v
        return ''.join(res)
