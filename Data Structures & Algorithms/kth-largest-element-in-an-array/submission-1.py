import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        res = []
        
        for i in nums:

            if len(res)<k:

                heapq.heappush(res,i)
            
            else:

                if i > res[0]:

                    heapq.heappushpop(res, i)
            
        return res[0]

        