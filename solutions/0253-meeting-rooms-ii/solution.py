class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        
        intervals = sorted(intervals, key = lambda x: x[0]) # O(nlogn)

        rooms = []

        heapq.heappush(rooms, intervals[0][1])

        for (start, end) in intervals[1:]:
            if start >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
        
        return len(rooms)


