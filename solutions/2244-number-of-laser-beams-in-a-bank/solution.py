class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_row_count = 0
        total = 0
        for row in bank:
            curr_row_count = sum(int(c) for c in row)
            if curr_row_count == 0:
                continue 
            total += curr_row_count * prev_row_count 
            prev_row_count = curr_row_count 
        return total 
