# Two Sum II - Input Array Is Sorted

class Solution(object):
    def twoSum(self, numbers, target):
        
        i = 0
        j = len(numbers)-1
        
        while i<j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] > target:
                j-=1
            else:
                i+=1
            
numbers = [2,7,11,15]
target = 9

obj = Solution()
print(obj.twoSum(numbers, target))        

# Time Complexity O(n)
# Space Complexity O(1)