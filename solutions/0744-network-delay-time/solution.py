from collections import deque, defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for (source, target, time) in times:
            graph[source].append((target,time))

        times_taken = [-1] * n 
        
        q = deque([(k,0)])

        times_taken[k-1] = 0

        while q:
            curr_node, curr_time = q.popleft()

            for (ngbr, time) in graph[curr_node]:
                time_ngbr = time + curr_time
                if times_taken[ngbr-1] == -1 or time_ngbr < times_taken[ngbr-1]:
                    times_taken[ngbr-1] = time_ngbr
                    q.append((ngbr, time_ngbr))
               

        return -1 if -1 in times_taken else max(times_taken)




