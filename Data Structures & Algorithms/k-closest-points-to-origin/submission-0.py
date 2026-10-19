import heapq, math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        data = []
        heapq.heapify(data)

        for x, y in points:

            euclidean = math.sqrt((x-0)**2 + (y-0)**2)
            heapq.heappush(data,[euclidean,x,y])
        
        res = []

        while len(res)<k:
            euclidean, x, y = heapq.heappop(data)
            res.append([x,y])
        
        return res


        