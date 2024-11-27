from collections import Counter
from heapq import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        task_counts = Counter(tasks)
        max_heap = [-count for count in task_counts.values()]
        heapify(max_heap)
        
        time = 0
        while max_heap:
            temp = []
            for _ in range(n + 1):
                if max_heap:
                    temp.append(heappop(max_heap))
            
            for task in temp:
                if task + 1 < 0:
                    heappush(max_heap, task + 1)
            
            time += n + 1 if max_heap else len(temp)

        return time
