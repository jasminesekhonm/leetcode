from collections import defaultdict

class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        
        # points = [[1,1],[1,3],[3,1],[3,3],[2,2]]

        xs = defaultdict(set)
        for (x, y) in points:
            xs[x].add(y)

        # 1: [1,3]
        # 3: [1,3]
        # 2: 2
        xvals = sorted(xs)
        min_area = float('inf')
        for a in range(len(xvals)):
            for b in range(a+1, len(xvals)):
                x0, x1 = xvals[a], xvals[b]
                ys = sorted(xs[x0] & xs[x1])
                if len(ys) >= 2:
                    min_height = min([ys[k+1]-ys[k] for k in range(len(ys)-1)])
                    min_area = min(min_area, min_height*(x1-x0))
        return min_area if min_area != float('inf') else 0
                
                    

            
            

       
            



        
