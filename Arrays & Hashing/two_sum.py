# Two Sum 

# def twoSum(nums, target):
    
#     for i in range(len(nums)):
        
#         for j in range(i+1, len(nums)):
#             if  nums[i] + nums[j] == target:
#                 return [i,j]

# nums = [4,2,3]
# target = 7
# print(twoSum(nums, target))

# Time Complexity O(n^2)
# Space Complexity O(1)

def twoSum(nums, target):
    
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_map:
            return [num_map[complement], i]
        
        else:
            num_map[num] = i

nums = [4,2,3]
target = 7
print(twoSum(nums, target))

# Time Complexity O(n)
# Space Complexity O(n)