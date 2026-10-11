from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        
        if len(nums) % k != 0:
            return False

        freq = Counter(nums)

        for start in sorted(freq):

            c = freq[start]
            if c == 0:
                continue
            for next in range(start,start+k):
                if freq[next] < c:
                    return False
                freq[next] -= c

        return True
        


