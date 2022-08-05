class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
        
        pointDict = defaultdict(set)
        for point in points:
            x, y = point 
            pointDict[x].add(y)
            
        
        pointDict = {k: sorted(v) for k, v in pointDict.items() if not len(v) < 2}
        
        minArea = float('inf')
        for k1, v1 in pointDict.items():
            for k2, v2 in pointDict.items():
                if k2 == k1:
                    continue 
                common_ys = [y for y in v1 if y in v2]
                if len(common_ys) < 2:
                    continue 
                minDiff = float('inf')
                for i in range(1, len(common_ys)):
                    diff = common_ys[i] - common_ys[i - 1]
                    if diff < minDiff:
                        minDiff = diff 
                        area = abs((k2 - k1) * diff)
                        minArea = min(area, minArea)
        return minArea if minArea != float('inf') else 0
                        
                        
                        
                    
                    
                
                
        
        
            
            
            
