class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []

        stack.append(len(temperatures)-1)
        res.append(0)

        for i in range(len(temperatures)-2, -1, -1):

            while len(stack)>0 and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()

            if len(stack) == 0:
                res.append(0)
                stack.append(i)

            else:
                res.append(stack[-1] - i)
                stack.append(i)

        return res[::-1]
                

            

