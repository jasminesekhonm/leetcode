from collections import deque

class Solution:
    def alienOrder(self, words: list[str]) -> str:
        
        graph = {c: [] for word in words for c in word}
        in_degrees = {c: 0 for word in words for c in word}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            
            for j in range(min(len(word1), len(word2))):
                parent, child = word1[j], word2[j]
                if parent != child:
                    in_degrees[child] += 1
                    graph[parent].append(child)
                    break

        
        q = deque([c for c in in_degrees if in_degrees[c] == 0])

        res = []
        while q:
            curr_char = q.popleft()
            res.append(curr_char)

            for child in graph[curr_char]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    q.append(child)
        
        return "" if len(res) != len(in_degrees) else "".join(res)

# O(V+E)

