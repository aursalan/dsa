from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):

        left,right, dq, max = 0,0, deque(), []

        while right<len(nums):

            while right-left+1 <= k:
                
                if len(dq)>0 and dq[0] < left:
                    dq.popleft()

                while len(dq) > 0 and nums[dq[-1]] < nums[right]:
                    dq.pop()
                
                dq.append(right)
                right+=1

            max.append(nums[dq[0]])
            left+=1
        
        return max
