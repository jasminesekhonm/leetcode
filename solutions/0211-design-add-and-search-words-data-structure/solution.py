class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root 
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word 
    
    def sub_search(self, node, sub_word) -> bool:
        for char in sub_word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return (node.word is not None)
            if word[i] == ".":
                return any([dfs(i + 1, child) for child in node.children.values()])
            else:
                return word[i] in node.children and dfs(i+1, node.children.get(word[i]))
                
        return dfs(0, self.root)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
