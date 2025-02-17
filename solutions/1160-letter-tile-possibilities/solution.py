class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequences = set()
        v = set()

        def bt(s, i):
            if s:
                sequences.add(s)
            if i == len(tiles):
                return 
            for j in range(len(tiles)):
                if j in v:
                    continue 
                v.add(j)
                bt(s+tiles[j], i+1)
                v.remove(j)
        bt('', 0)
        return len(sequences)
