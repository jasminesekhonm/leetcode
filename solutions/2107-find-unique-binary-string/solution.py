class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums.sort() # O(nlogn)
        n = len(nums)
        def generate(curr):
            if len(curr) == n:
                if curr in nums:
                    return ""
                return curr 
            add_zero = generate(curr + "0")
            if add_zero:
                return add_zero
            return generate(curr + "1")
    
        nums = set(nums)
        return generate("")
        
