class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        
        n = len(heights)

        if n == 0:
            return 0
        
        elif n == 1:
            return [0]

        stack = []

        ans = [0] * n 

        for i in range(n):
            height = heights[i]
            while stack and heights[stack[-1]] < height:
                ans[stack.pop()] += 1
            if stack:
                ans[stack[-1]] += 1
            stack.append(i)
        
        return ans

