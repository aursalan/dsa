import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = Counter(tasks)
        heap = []

        for task, freq in counter.items():
            heapq.heappush_max(heap, (freq, task))
        
        cooldown = deque()
        time = 0

        while heap or cooldown:
            time += 1

            if heap: 
                freq, task = heapq.heappop_max(heap)
                freq -=1

                if freq > 0:
                    cooldown.append((freq, task, time+n))

            while cooldown and cooldown[0][2] <= time:
                freq, task, release_time = cooldown.popleft()
                heapq.heappush_max(heap, (freq, task))

        return time
                


            



        
            


        