class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m, n = len(mat), len(mat[0])

        sums = defaultdict(int)

        for i in range(m):
            sum_i = sum(mat[i])
            sums[i] = sum_i 
            
        indices = [row for row, v in sorted(sums.items(), key=lambda x: x[1])]
        return indices[:k]
        
        
