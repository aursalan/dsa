class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if nums[len(nums)-1] > nums[0] or len(nums) == 1:
            return nums[0]

        left = len(nums)-1
        right = 0
        mid = 0

        while left > right:

            mid = (left+right) // 2

            if nums[mid] > nums[right]:
                right = mid
            else:
                left = mid

        
        return nums[mid+1]