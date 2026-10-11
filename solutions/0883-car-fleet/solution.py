class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        n_fleets = 0

        slowest = None 

        for (p, s) in sorted(zip(position, speed), reverse=True):
            time_to_target = (target - p) / s 
            if not slowest or time_to_target > slowest:
                slowest = time_to_target 
                n_fleets += 1

        return n_fleets
