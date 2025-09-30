# Product of Array Except Self

# class Solution():
#     def productExceptSelf(self, nums):
        
#         res = [1 for _ in range(len(nums))]
        
#         for i in range(len(nums)):
            
#             for j in range(len(nums)):
                
#                 if j == i:
#                     continue
                
#                 res[j] *= nums[i]
                
#         return res


# nums = [1,2,3,4]

# obj = Solution()

# print(obj.productExceptSelf(nums))

# Time Complexity O(n^2)
# Space Complexity O(n)

class Solution():
    def productExceptSelf(self, nums):
        
        res = [1 for _ in range(len(nums))]
        prefix_product = 1
        postfix_product = 1
        
        for i in range(len(nums)):
            
            res[i] = prefix_product
            prefix_product *= nums[i]
        
        for j in range(len(nums)-1, -1, -1):

            res[j] *= postfix_product
            postfix_product *= nums[j]
            
        return res

nums = [1,2,3,4]

obj = Solution()

print(obj.productExceptSelf(nums))

# Time Complexity O(n)
# Space Complexity O(1)