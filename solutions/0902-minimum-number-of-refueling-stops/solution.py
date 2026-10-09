class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:

        stations.append([target, 0])

        curr_fuel = startFuel 

        n_stops = 0
        prev_pos = 0

        stations_missed = []

        for (pos, fuel) in stations:
            dist = pos - prev_pos
            remaining_fuel = curr_fuel - dist 

            if remaining_fuel < 0:
                while stations_missed and remaining_fuel < 0:
                    remaining_fuel += -heapq.heappop(stations_missed) 
                    n_stops += 1
                
                if remaining_fuel < 0:
                    return -1 

            curr_fuel = remaining_fuel 
            prev_pos = pos
            heapq.heappush(stations_missed, -fuel)

        return n_stops
        
