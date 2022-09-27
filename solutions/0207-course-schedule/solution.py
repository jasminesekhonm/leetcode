class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courseGraph = defaultdict(list)
        inDegrees = defaultdict(int)
        
        for (course, prereq) in prerequisites:
            courseGraph[prereq].append(course)
            inDegrees[course] = inDegrees.get(course, 0) + 1
         
        q = deque()
        visited = set()
        
        for course in range(numCourses):
            if course not in inDegrees:
                q.append(course)
        
        while q:
            currCourse = q.popleft()
            visited.add(currCourse)
            
            for nextCourse in courseGraph[currCourse]:
                if not nextCourse in visited:
                    inDegrees[nextCourse] -= 1
                    if inDegrees[nextCourse] == 0:
                        q.append(nextCourse)
        
        return len(visited) == numCourses

