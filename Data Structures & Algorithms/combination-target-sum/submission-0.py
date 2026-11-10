class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []

        def backtrack(index, remainder):

            if remainder == 0:
                res.append(subset.copy())
                return 
            
            if remainder < 0:
                return
            
            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtrack(i, remainder-nums[i])
                subset.pop()
        
        backtrack(0,target)

        return res
