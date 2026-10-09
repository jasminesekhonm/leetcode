class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        cars = zip(position, speed)
        cars = sorted(cars, key = lambda x: x[0])

        slowest = None
        n_fleets = 0

        for i in range(len(cars)-1, -1, -1):
            pos, speed = cars[i][0], cars[i][1]
            time = (target - pos) / speed
            if slowest is None or time > slowest:
                slowest = time 
                n_fleets += 1
        
        return n_fleets
            
