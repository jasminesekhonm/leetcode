class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:

        if len(intervals) <= 1:
            return True
            
        intervals = sorted(intervals, key = lambda x: x[0]) 


        curr_start, curr_end = intervals[0][0], intervals[0][1]

        for interval in intervals[1:]:
            start, end = interval[0], interval[1]
            if start < curr_end: # new meeting starts before previous ends
                return False
            if (start == curr_start):
                return False
            curr_end = max(end, curr_end) # latest meetings end
            curr_start = min(curr_start, start) # earliest meetings start

        return True

        
