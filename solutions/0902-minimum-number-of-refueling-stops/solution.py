class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        
        stations.append((target,float('inf')))

        curr_fuel = startFuel
        curr_pos = 0

        skipped = []

        n_stops = 0

        for (pos, fuel) in stations:
            dist = pos - curr_pos
            rem_fuel = curr_fuel - dist 
            while skipped and rem_fuel < 0:
                rem_fuel -= heapq.heappop(skipped)
                n_stops += 1
            if rem_fuel < 0:
                return -1
            curr_fuel = rem_fuel 
            curr_pos = pos 
            heapq.heappush(skipped, -fuel)

        return n_stops 



