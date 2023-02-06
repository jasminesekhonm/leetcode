class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals, key = lambda x: x[0])

        newIntervals = []

        currStart, currEnd = intervals[0]

        for interval in intervals[1:]:
            newStart, newEnd = interval 

            # currStart, currEnd, newStart, newEnd
            # -- append [currStart, currEnd] to list of new intervals 
            # --- currStart, currEnd = newStart, newEnd
            # currStart, newStart, currEnd, newEnd 
            # --- currStart, currEnd  = [currStart, newEnd]
            # currStart, newStart, newEnd, currEnd 
            # --- currStart, currEnd = [currStart, currEnd]

            if currStart <= currEnd < newStart <= newEnd: 
                newIntervals.append([currStart, currEnd])
                currStart, currEnd = newStart, newEnd 
            
            elif currStart <= newStart <= currEnd <= newEnd:
                currStart, currEnd = currStart, newEnd 

            elif currStart <= newStart <= newEnd <= currEnd:
                currStart, currEnd = currStart, currEnd 
        
        newIntervals.append([currStart, currEnd])
        return newIntervals

            

