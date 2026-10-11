class Solution:
    def trap(self, heights: list[int]) -> int:
        
        stack = []

        ans = 0

        for i, height in enumerate(heights):
            while stack and height > heights[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break
                start_index = stack[-1]
                c_width = i - start_index -1
                c_height = min(height, heights[start_index]) - heights[bottom]
                ans += (c_width * c_height)
                
            stack.append(i)

        return ans

