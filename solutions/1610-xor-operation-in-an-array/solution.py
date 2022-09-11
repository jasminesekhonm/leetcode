class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # nums[i] = start + 2 * i 
        
        ans = 0
        nums = [start + 2 * i for i in range(n)]
        
        for num in nums:
            ans = ans ^ num
            
        return ans
            
            
            
        
