from collections import Counter

class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:

        n = len(nums)

        if n % k != 0:
            return False

        freq = Counter(nums)

        for num in sorted(freq):
            count = freq[num]
            if count == 0:
                continue 
            for x in range(num, num+k):
                if freq[x] < count:
                    return False
                freq[x] -= count

        return True

