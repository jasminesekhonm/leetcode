class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        n_fleets, slowest = 0, 0 

        for (pos, speed) in cars:
            time = (target - pos) / speed 
            if time > slowest:
                slowest = time
                n_fleets += 1 

        return n_fleets
        
