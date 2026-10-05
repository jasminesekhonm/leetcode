class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals = sorted(intervals, key=lambda x: x[0])

        def merge_overlap(interval1, interval2):
            start1, end1 = interval1
            start2, end2 = interval2 
            start = min(start1, start2)
            end = max(end1, end2)
            return [start, end]

        res = [intervals[0]]
        prev_start, prev_end = intervals[0]
        for interval in intervals[1:]:
            curr_start, curr_end = interval[0], interval[1]
            if curr_start > prev_end:
                res.append(interval)
                prev_start, prev_end = interval
            
            else:
                prev_interval = res.pop()
                new_interval = merge_overlap(prev_interval, interval)
                res.append(new_interval)
            
                prev_start, prev_end = new_interval
        
        return res



        
