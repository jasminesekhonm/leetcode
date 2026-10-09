class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        # [4,2,3,1]

        n = len(heights)

        max_height = heights[-1]

        ans = [n-1]

        for i in range(n-2, -1, -1):
            if heights[i] > max_height:
                ans.append(i)
                max_height = heights[i]

        ans.reverse()
        return ans

        
