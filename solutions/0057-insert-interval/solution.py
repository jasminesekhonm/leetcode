class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        if len(intervals) == 0:
            return [newInterval]

        ans = []
        n = len(intervals)
        new_start, new_end = newInterval[0], newInterval[1]

        i = 0 
        while i < n and intervals[i][1] < new_start:
            ans.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        
        ans.append([new_start, new_end])

        while i < n:
            ans.append(intervals[i])
            i += 1
        
        return ans 

