class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        prefix =[]
        stack = []

        for i in range(len(heights)):

            while stack and stack[-1][0] >= heights[i]:
                stack.pop()

            if stack: 
                prefix.append((stack[-1][1]))

            else: 
                prefix.append(-1)
            
            stack.append((heights[i],i))

        suffix = []
        stack = []

        for i in range(len(heights)-1,-1,-1):

            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            
            if stack:
                suffix.append((stack[-1][1]))
            else:
                suffix.append(len(heights))
            
            stack.append((heights[i],i))

        suffix = suffix[::-1]

        largestArea = float('-inf')

        for i in range(len(heights)):

            left = prefix[i] + 1
            right = suffix [i] - 1
            width = ( right - left ) + 1

            largestArea = max(width * heights[i], largestArea)

        return largestArea
        