class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates = sorted(candidates)

        subset = [] 
        res = []

        def backtrack(index, remaining):

            if remaining == 0:
                res.append(subset.copy())
                return 

            for i in range(index, len(candidates)):

                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                if candidates[i] > remaining:
                    break
                
                subset.append(candidates[i])

                backtrack(i + 1, remaining - candidates[i])

                subset.pop()

        backtrack(0, target)

        return res