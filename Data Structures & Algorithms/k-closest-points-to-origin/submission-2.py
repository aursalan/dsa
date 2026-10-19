import heapq, math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        data = []

        for x, y in points:

            euclidean = math.sqrt((x-0)**2 + (y-0)**2)

            if len(data)<k:
                heapq.heappush_max(data,[euclidean,x,y])
            
            else:
                
                maxEuclidean = data[0][0]

                if euclidean < maxEuclidean:
                    heapq.heappushpop_max(data,[euclidean,x,y])
                
        return [[x, y] for e,x,y in data]

    

                


        