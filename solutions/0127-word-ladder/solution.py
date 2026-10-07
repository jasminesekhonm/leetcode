from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0 
        
        q = deque([(beginWord, 1)])

        wordList = set(wordList)
        
        while q:
            curr_word, n_seq = q.popleft()
            if curr_word == endWord:
                return n_seq
            
            for i, char in enumerate(curr_word):
                for replacement in "abcdefghijklmnopqrstuvwxyz":
                    new_word = curr_word[:i] + replacement + curr_word[i+1:]
                    if new_word in wordList:
                        wordList.remove(new_word)
                        q.append((new_word, n_seq+1))

        return 0


        

        
