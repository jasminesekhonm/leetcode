from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        graph = defaultdict(list)
        in_degrees = {c: 0 for c in range(numCourses)}

        for (a, b) in prerequisites:
            graph[b].append(a)
            in_degrees[a] += 1

        q = []

        ans = []

        for course in in_degrees:
            if in_degrees[course] == 0:
                q.append(course)
                ans.append(course)
                
        
        while q:
            curr_course = q.pop()
            for next_course in graph[curr_course]:
                in_degrees[next_course] -= 1 
                if in_degrees[next_course] == 0:
                    q.append(next_course)
                    ans.append(next_course)

        return ans if len(ans) == numCourses else []

        
        
        # Time Complexity: O(numCourses + len(prerequisites))
        # Space Complexity: O(numCourses + len(prerequisites))

        

        
