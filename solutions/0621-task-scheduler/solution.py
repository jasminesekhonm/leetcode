class Solution(object):
    def leastInterval(self, tasks, n):
        task_counts = [0] * 26
        
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1
        
        task_counts.sort(reverse=True)
        
        max_freq = task_counts[0]
        
        max_count = task_counts.count(max_freq)
        
        min_intervals = (max_freq - 1) * (n + 1) + max_count
        
        return max(min_intervals, len(tasks))
