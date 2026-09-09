class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles) 
        
        while left < right:
            
            mid = (right+left) // 2

            consumedHours = self.countHours(piles,mid)

            if consumedHours <= h:
                right = mid 
            
            else:
                left = mid + 1
            
        return left

    def countHours(self, piles: List[int], k: int) -> int:

        count = 0

        for i in piles:

            if i <= k:

                count += 1
            
            else:
                
                quotient = i // k
                remainder = i % k 

                count += quotient
                
                if remainder!=0: 
                    count +=1 

        return count 