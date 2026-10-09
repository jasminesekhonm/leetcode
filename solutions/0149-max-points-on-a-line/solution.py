from collections import defaultdict

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        
        if len(points) == 0:
            return 0

        ans = 1
        for i in range(len(points)):
            x1, y1 = points[i]
            slope_dict = defaultdict(int)
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                if x2 == x1:
                    slope = "V"
                elif y2 == y1:
                    slope = "H"
                else:
                    slope = (y2-y1) / (x2-x1) 
                slope_dict[slope] += 1
            if len(slope_dict) > 0:
                max_slope = max(slope_dict.values()) + 1
                ans = max(ans, max_slope)
        
        return ans 
        
