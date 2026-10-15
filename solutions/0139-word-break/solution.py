class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    def search(self, word):
        node = self.root 
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        
        num_words = len(wordDict)
        
        n = len(s)

        trie = Trie()

        for word in wordDict:
            trie.insert(word)

        
        node = trie.root 

        @cache
        def dfs(node, index):
            if index == len(s):
                return node.is_end

            if node.is_end and dfs(trie.root, index):
                return True
            
            char = s[index]
            if char not in node.children:
                return False
            
            node = node.children[char]
            return dfs(node, index+1)

        return dfs(trie.root, 0)





        
