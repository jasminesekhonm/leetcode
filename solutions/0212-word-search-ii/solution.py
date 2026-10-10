class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.word = word 


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m, n = len(board), len(board[0])

        
        found = set()
        moves = [(1,0), (0,1), (-1,0), (0,-1)]

        trie = Trie()
        for word in words:
            trie.insert(word)

        def is_valid(r,c):
            return (0 <= r < m) and (0 <= c < n)

        def dfs(r, c, parent):
            char = board[r][c]
            node = parent.children.get(char)

            if node.word:
                found.add(node.word)
                node.word = None
            
            board[r][c] = "#"
            for (dr, dc) in moves:
                nr, nc = r + dr, c + dc 
                if not is_valid(nr, nc):
                    continue 
                if board[nr][nc] in node.children:
                    dfs(nr, nc, node)
            
            board[r][c] = char 
            if not node.children and not node.word:
                del parent.children[char]
            
            
        for i in range(m):
            for j in range(n):
                char = board[i][j]
                if char in trie.root.children:
                    dfs(i, j, trie.root)
    

        
        return list(found)
    

