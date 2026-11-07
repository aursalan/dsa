class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        for i in nums:

            for j in range(len(res)):

                newList = []
                newList.extend(res[j])
                newList.append(i)

                res.append(newList)

            res.append([i])
        
        res.append([])
        
        return res

