class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        res = []
        start1, end1 = intervals[0]
        currInterval = [start1, end1]
        for (start2, end2) in intervals[1:]:
            if start2 <= end1 and end1 <= end2:
                currInterval = [start1, end2]
                start1, end1 = start1, end2
            elif start2 <= end1 and end2 <= end1:
                currInterval = [start1, end1]
                start1, end1 = start1, end1
            else:
                res.append(currInterval)
                start1, end1 = start2, end2
                currInterval = [start1, end1]
        
        res.append(currInterval)
        return res
                
