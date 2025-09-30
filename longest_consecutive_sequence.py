# Longest Consecutive Sequence

class Solution(object):
    def longestConsecutive(self, nums):
        
        nums_set = set(nums)
        longest = 0
        
        for num in nums_set:
            
            if (num-1) not in nums_set:
                curr = num
                curr_longest = 1
                
                while ( curr + 1) in nums_set:
                    curr +=1
                    curr_longest +=1
        
                longest = max(longest, curr_longest)
        
        return longest

nums = [100,4,200,1,2,3]
obj = Solution()
print(obj.longestConsecutive(nums))

# Time Complexity O(n)
# Space Complexity O(n)
            