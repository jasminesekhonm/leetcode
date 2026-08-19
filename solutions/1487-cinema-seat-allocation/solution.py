import collections

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        reservedSeatsDict = collections.defaultdict(int)

        for (row, seat) in reservedSeats:
            if 2 <= seat <= 9:
                reservedSeatsDict[row] |= (1 << (seat-2))

        LEFT = 0b11110000   # Seats 2,3,4,5
        MIDDLE = 0b00111100 # Seats 4,5,6,7
        RIGHT = 0b00001111 # Seats 6,7,8,9

        ans = 2*n

        for row in reservedSeatsDict:
            ans -= 2
            row_mask = reservedSeatsDict[row]
            if (row_mask & LEFT) == 0 and (row_mask & RIGHT) == 0:
                ans += 2
            elif (row_mask & LEFT) == 0 or (row_mask & MIDDLE) == 0 or (row_mask & RIGHT) == 0:
                ans += 1
    
        return ans
