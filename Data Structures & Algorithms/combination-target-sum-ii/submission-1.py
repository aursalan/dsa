class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates = sorted(candidates)

        subset = [] 
        res = []

        def backtrack(index, remaining):

            if remaining == 0:
                res.append(subset.copy())
                return 

            if index == len(candidates):
                return
            
            if remaining < 0:
                return 
            
            subset.append(candidates[index])
            backtrack(index+1, remaining-candidates[index])
            
            subset.pop()

            nextIndex = index+1
            
            while nextIndex < len(candidates) and candidates[nextIndex] == candidates[index]:
                nextIndex+=1

            backtrack(nextIndex, remaining)

        backtrack(0, target)

        return res