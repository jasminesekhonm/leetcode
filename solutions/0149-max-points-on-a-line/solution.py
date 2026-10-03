class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        
        def get_slope(p1, p2):
            x1, y1 = p1 
            x2, y2 = p2 
            if (x2 == x1):
                return "V"
            elif (y1 == y2):
                return "H"
            return (y2 - y1) / (x2 - x1)


        num_points = len(points)
        
        best = 1
        for i in range(num_points):
            p1 = points[i]
            freq_dict = {}
        
            for j in range(i+1, num_points):
                p2 = points[j]

                slope = get_slope(p1, p2)
                freq_dict[slope] = freq_dict.get(slope, 0) + 1 
            if freq_dict:
                best = max(best, max(freq_dict.values()) + 1)
        return best
