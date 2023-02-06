class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rightProducts = [1 for _ in range(n)]
        leftProducts = [1 for _ in range(n)]

        for i in range(n-1):
            rightProducts[i+1] = nums[i] * rightProducts[i]
        
        for i in range(n-1, 0, -1):
            leftProducts[i-1] = nums[i] * leftProducts[i]

        res = []

        for i in range(n):
            res.append(rightProducts[i] * leftProducts[i])

        return res 


        
        
        

