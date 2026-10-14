class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[1])

        n_removed = 0

        prev_end = -inf
        for (start, end) in intervals:
            if start >= prev_end:
                prev_end = end 
            else:
                n_removed += 1
        
        return n_removed


