from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = {n: [] for n in range(numCourses)}
        inDegree = {n: 0 for n in range(numCourses)}
        for (a, b) in prerequisites:
            graph[a].append(b)
            inDegree[b] += 1

        
        q = deque([n for n in range(numCourses) if inDegree[n] == 0])
        
        taken = 0
        while q:
            course = q.popleft()
            taken += 1
            for ngbr in graph[course]:
                inDegree[ngbr] -= 1
                if inDegree[ngbr] == 0:
                    q.append(ngbr)
            
        return taken == numCourses

        return False

            


