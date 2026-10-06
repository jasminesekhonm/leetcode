from collections import deque

class Solution:
    def alienOrder(self, words: list[str]) -> str:

        in_degrees = {c: 0 for word in words for c in word}
        graph = {c: [] for word in words for c in word}

        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for j in range(0, min(len(w1), len(w2))):
                parent, child = w1[j], w2[j]
                if parent != child:
                    in_degrees[child] += 1
                    graph[parent].append(child)
                    break
                

        
        q = deque([char for char in in_degrees if in_degrees[char] == 0])
        res = []
        while q:
            curr_char = q.popleft()
            res.append(curr_char)

            for child in graph[curr_char]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    q.append(child)
            
        
        if len(res) != len(in_degrees):
            return ""

        return "".join(res)

        
