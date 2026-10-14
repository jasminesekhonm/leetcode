class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        
        m, n = len(firstList), len(secondList)

        intersection = []

        i, j = 0, 0

        while i < m and j < n:
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            lo = max(start1, start2)
            hi = min(end1, end2)

            if lo <= hi:
                intersection.append([lo, hi])
            
            if end1 < end2:
                i += 1
            else:
                j += 1
        
        return intersection
