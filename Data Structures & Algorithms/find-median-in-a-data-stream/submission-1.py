import heapq 

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:

        if len(self.left) == 0:
            heapq.heappush_max(self.left, num)
            return
        
        heapq.heappush_max(self.left, num)
        
        if len(self.left) > len(self.right):
            heapq.heappush(self.right, heapq.heappop_max(self.left))

            if len(self.right) > len(self.left):
                heapq.heappush_max(self.left, heapq.heappop(self.right))
            

    def findMedian(self) -> float:

        if (len(self.left) + len(self.right)) % 2 !=0:

            return self.left[0]
        
        else:

            return (self.left[0] + self.right[0]) / 2
        
        