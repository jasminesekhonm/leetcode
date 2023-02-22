class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        m, n = len(image), len(image[0])

        moves = [(1,0),(0,1),(0,-1),(-1,0)]

        q = [(sr, sc)]

        visited = set()

        src_color = image[sr][sc]
        while q:
            row, col = q.pop()
            visited.add((row, col))
            image[row][col] = color 
            for (dRow, dCol) in moves:
                newRow, newCol = row + dRow, col + dCol 
                if 0 <= newRow < m and 0 <= newCol < n and image[newRow][newCol] == src_color and (newRow, newCol) not in visited:
                    q.append((newRow, newCol)) 
                    

        return image 

