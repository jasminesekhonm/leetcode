class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        
        if len(points) == 0:
            return 0 
        
        if len(points) <= 2:
            return len(points)

        points = sorted(points, key = lambda x: x[0])
        
        max_points = 1

        for i in range(len(points)):
            slope_dict = {}
            x1, y1 = points[i][0], points[i][1]
            for j in range(i+1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                if (x2 == x1):
                    slope_dict['V'] = slope_dict.get('V', 0) + 1
                elif (y2 == y1):
                    slope_dict['H'] = slope_dict.get('H', 0) + 1
                else:
                    slope = (y2 - y1) / (x2 - x1)
                    slope_dict[slope] = slope_dict.get(slope, 0) + 1
            if len(slope_dict) > 0:
                max_points = max(max_points, max(slope_dict.values())+1)
        return max_points


                
        

