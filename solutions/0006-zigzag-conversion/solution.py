class Solution:
    def convert(self, s: str, numRows: int) -> str:

        n = len(s)
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        r, step = 0, 1
        for char in s:
            rows[r].append(char)
            if (r == 0) and (step == -1):
                step = 1
            elif (r == numRows-1) and (step == 1):
                step = -1
            r = r + step
        
        return "".join("".join(row) for row in rows)

        
