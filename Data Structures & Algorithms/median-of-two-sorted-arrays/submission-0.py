class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        length = len(nums1) + len(nums2)
        leftSize = ( length + 1) // 2
        
        left = 0
        right = len(nums1)

        while left <= right:

            mid = (left + right) // 2

            nums1_left = nums1[mid-1] if mid > 0 else float('-inf')
            nums1_right = nums1[mid] if mid < len(nums1) else float('inf')

            nums2_left = nums2[leftSize-mid-1] if (leftSize-mid) > 0 else float('-inf')
            nums2_right = nums2[leftSize-mid] if (leftSize-mid) < len(nums2) else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:

                if length % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                
                else:
                    return max(nums1_left, nums2_left)
            
            elif nums1_left > nums2_right:
                right = mid - 1
            
            else:
                left = mid + 1
        

        