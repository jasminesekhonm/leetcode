class TrieNode:
    def __init__(self):
        self.is_end = False
        self.w = None 
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        node.w = word 

    def search(self, word):
        node = self.root 
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children
        return node.is_end 
    def startsWith(self, prefix):
        node = self.root 
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children
        return True 

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        m, n = len(board), len(board[0])
        res = set()
        trie = Trie()
        
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for w in words:
            trie.insert(w)

        
        def dfs(r, c, parent_node):
            ch = board[r][c]
            if ch not in parent_node.children:
                return None 
            node = parent_node.children.get(ch)
            if node.w:
                res.add(node.w)
                node.w = None
            board[r][c] = "#"   
            for (dr, dc) in moves:
                nr, nc = r + dr, c + dc 
                if 0 <= nr < m and 0 <= nc < n:
                    dfs(nr, nc, node)
            board[r][c] = ch
            if not node.children and not node.w:
                del parent_node.children[ch]
            

        for r in range(m):
            for c in range(n):
                dfs(r, c,trie.root)
        
        return list(res)



        

