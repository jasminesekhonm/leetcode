class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        
        n = len(heights)

        res = [0] * n

        stack = []
        # [10,6,8,5,11,9]
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] < height:
                res[stack.pop()] += 1
            if stack:
                res[stack[-1]] += 1
            
            stack.append(i)
        
        return res





            
            


