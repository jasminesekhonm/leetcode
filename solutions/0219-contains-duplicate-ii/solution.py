class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freqDict = defaultdict(int)
        for i, num in enumerate(nums):
            if num in freqDict and abs(i-freqDict[num]) <= k:
                return True 
            else:
                freqDict[num] = i 
        
        return False
        
