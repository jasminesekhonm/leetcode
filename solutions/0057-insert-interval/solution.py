class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x: x[0])

        new_intervals = []

        for (start, end) in intervals:
            while new_intervals and start <= new_intervals[-1][1]:
                prev_start, prev_end = new_intervals.pop()
                start = min(prev_start, start)
                end = max(prev_end, end)
            new_intervals.append([start, end])

        return new_intervals

