class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l, r = 0, len(matrix) - 1 

        while l<=r:

            mid = (r+l)//2

            if target == matrix[mid][0]:
                return True
            
            elif target < matrix[mid][0]:
                r = mid - 1 

            else: 

                if mid == len(matrix) - 1 or target < matrix[mid+1][0]:

                    left, right = 0, len(matrix[0]) - 1 

                    while left <= right:

                        secondMid = (right+left)//2
                        
                        if target == matrix[mid][secondMid]:
                            return True
                        
                        elif target < matrix[mid][secondMid]:
                            right = secondMid - 1

                        else:
                            left = secondMid + 1
                        
                    return False
                        
                else:

                    l = mid + 1

        return False

        