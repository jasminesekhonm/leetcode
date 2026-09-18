class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        def find_slope(point1, point2):
            dx = point2[0] - point1[0]
            dy = point2[1] - point1[1]

            if dx == 0:
                return inf
            return dy / dx
        
        ans = 1 

        for i, point1 in enumerate(points):
            slopes = defaultdict(int)
            for j, point2 in enumerate(points[i+1:]):
                slope = find_slope(point1, point2)
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans+1
