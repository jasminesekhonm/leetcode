class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        
        def distance(point):
            return point[0]**2 + point[1]**2 

        def split_by_distance(remaining, mid):
            closer, farther = [], []

            for index in remaining:
                if distances[index] <= mid:
                    closer.append(index)
                else:
                    farther.append(index)
            return closer, farther

        distances = [distance(point) for point in points]
        remaining = [i for i in range(len(points))]

        l, h = 0, max(distances)

        ans = []
        while k:
            mid = (l + h) / 2
            closer, farther = split_by_distance(remaining, mid)
            if len(closer) > k:
                remaining = closer
                h = mid 
            else:
                ans.extend(closer)
                k -= len(closer)
                remaining = farther
                l = mid 

        return [points[i] for i in ans]




