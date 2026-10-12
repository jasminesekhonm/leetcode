class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        intervals = sorted(intervals, key = lambda x: x[0])
        stack = []

        for (start, end) in intervals:
            while stack and stack[-1][1] >= start:
                curr_start, curr_end = stack.pop()
                start = min(curr_start, start)
                end = max(curr_end, end)
            stack.append((start, end))
        
        return stack

