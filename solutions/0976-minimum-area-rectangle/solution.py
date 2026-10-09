from collections import defaultdict

class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        
        if len(points) < 4:
            return 0

        xcoords = defaultdict(set)

        for (x,y) in points:
            xcoords[x].add(y)

        
        xvals = sorted(xcoords)
        min_area = float('inf')

        for i in range(len(xvals)):
            x1 = xvals[i]
            for j in range(i+1, len(xvals)):
                x2 = xvals[j]
                y1s = xcoords[x1]
                y2s = xcoords[x2]
                ys = sorted(y1s & y2s)
                if len(ys) < 2:
                    continue 
                width = abs(x2-x1)
                min_height = min([abs(ys[i+1]-ys[i]) for i in range(len(ys)-1) ])
                min_area = min(min_height * width, min_area)

        return min_area if min_area != float('inf') else 0




        
