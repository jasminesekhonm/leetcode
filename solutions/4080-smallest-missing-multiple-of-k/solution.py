class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        
        visited = set(nums)
        
        ans = k 

        while ans in visited:
            ans += k
        
        return ans
        
