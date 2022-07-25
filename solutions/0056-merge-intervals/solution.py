class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key = lambda x: x[0])
        i = 0 
        current_start = intervals[0][0]
        current_end = intervals[0][1]
        # given two intervals sorted by their start time
        # [a1, b1], [a2, b2] a1 < a2
        # [a2, b2] can be entirely consumed by [a1, b1] --> a1 < a2 < b2 < b1 
        # [a2, b2] can partially overlap [a1, b1] --> a1 < a2 < b1 < b2
        # [a2, b2] can be entirely disjoint from [a1, b1] --> a1 < b1 < a2 < b2
        intervals_ = []
        while i < len(intervals):
            if current_start <= intervals[i][0] <= current_end <= intervals[i][1]:
                current_end = intervals[i][1]
            elif current_start <= current_end < intervals[i][0] <= intervals[i][1]:
                intervals_.append([current_start, current_end])
                current_start = intervals[i][0]
                current_end = intervals[i][1]
            i = i + 1 
        intervals_.append([current_start, current_end])
        return intervals_
                
                
        
