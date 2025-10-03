# 3Sum

class Solution(object):
    def threeSum(self, nums):
        
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    res.append([nums[i],nums[j],nums[k]])
                    
                    while j<k and nums[j] == nums[j+1]:
                        j+=1
                    while j<k and nums[k] == nums[k-1]:
                        k-=1
                    
                    j+=1
                    k-=1
                    
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                    
                else:
                    j+=1
        return res
        
nums = [-1,0,1,2,-1,-4]
obj = Solution()
print(obj.threeSum(nums))

# Time Complexity O(n^2)
# Space Complexity O(1)