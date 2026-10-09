class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:

        n = len(heights)

        lefts = [-1] * n 
        rights = [n] * n

        stack = []

        for i in range(n):
            height = heights[i]
            while stack and heights[stack[-1]] >= height:
                stack.pop()
            lefts[i] = stack[-1] + 1 if stack else 0
            stack.append(i)
        
        stack = []
        for i in range(n-1, -1, -1):
            height = heights[i]
            while stack and heights[stack[-1]] >= height:
                stack.pop()
            rights[i] = stack[-1] if stack else n
            stack.append(i)
        
        max_area = 0
        for i in range(n):
            max_area = max(max_area, heights[i] * (rights[i] - lefts[i]))
        
        return max_area



            
        
