import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapq.heapify_max(stones)

        while stones:

            if len(stones)==1:
                break

            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)

            if x == y:
                continue
            
            else:
                heapq.heappush_max(stones, y-x)
        
        if len(stones) == 1:
            return stones[0]
        
        return 0
            

                





        