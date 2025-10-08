class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0]) # O(nlogn)
        result = []
        start, end = intervals[0][0], intervals[0][1]
        for interval in intervals[1:]:
            newStart, newEnd = interval[0], interval[1]
            if newStart <= end and newEnd > end:
                end = newEnd 
            elif newStart > end:
                result.append([start, end])
                start, end = newStart, newEnd
                
            # start = newStart 
        result.append([start, end])
        return result


