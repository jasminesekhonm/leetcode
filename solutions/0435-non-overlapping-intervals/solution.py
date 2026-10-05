class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        n = len(intervals)

        if len(intervals) <= 1:
            return 0 

        prev_start, prev_end = intervals[0]
        removed = 0
        for interval in intervals[1:]:
            start, end = interval
            if start < prev_end:
                removed += 1
                prev_end = min(end, prev_end)
            else:
                prev_end = end 

        return removed

