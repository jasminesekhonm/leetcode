class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        
        intervals = sorted(intervals, key = lambda x: x[0]) # O(nlogn)

        if len(intervals) <= 1:
            return True

        _, curr_end = intervals[0]
        for (start, end) in intervals[1:]:
            if start < curr_end:
                return False
            curr_end = end

        return True



