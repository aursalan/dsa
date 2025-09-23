# Top K Frequent Elements

# def topKFrequent(nums, k):
    
#     nums.sort()
#     count = 1
#     i = 0
#     nums_map = {}
#     res = []
    
#     while i <= len(nums)-1:
        
#         if i< len(nums)-1 and nums[i] == nums[i+1]:
#             count +=1
#             i +=1
            
#         else:
#             nums_map[nums[i]] = count
#             count = 1
#             i +=1
        
#     while len(res) != k:
        
#         temp = largestElement(nums_map)
        
#         if temp not in res:
#             res.append(temp)
#             nums_map.pop(temp)
        
#     return res

# def largestElement(nums_map):
    
#     max_freq = float('-inf')
#     element_with_max_freq = None

#     for num, frequency in nums_map.items():
        
#         if frequency > max_freq:
#             max_freq = frequency
#             element_with_max_freq = num
            
#     return element_with_max_freq

# nums = [1,1,1,1,2,2,2,3,3,4]
# k = 2

# print(topKFrequent(nums, k))

# Time Complexity O(n log n + k . m)
# Space Complexity O(m)

# def topKFrequent(nums, k):
    
#     nums_map = {}
    
#     for i in nums:
        
#         if i in nums_map:
#             nums_map[i] += 1
            
#         else:
#             nums_map[i] = 1        
    
#     res = []
    
#     while len(res) != k:
        
#         temp = largestElement(nums_map)
        
#         if temp not in res:
#             res.append(temp)
#             nums_map.pop(temp)
        
#     return res

# def largestElement(nums_map):
    
#     max_freq = float('-inf')
#     element_with_max_freq = None

#     for num, frequency in nums_map.items():
        
#         if frequency > max_freq:
#             max_freq = frequency
#             element_with_max_freq = num
            
#     return element_with_max_freq
        
# nums = [1,2,1,2,1,2,3,1,3,2]
# k = 2

# print(topKFrequent(nums, k))

# # Time Complexity O(n + k . m)
# # Space Complexity O(m)

# from collections import Counter 
# import heapq

# def topKFrequent(nums, k):
    
#     nums_map = Counter(nums)
#     min_heap = []
    
#     for num, freq in nums_map.items():
#         heapq.heappush(min_heap, (freq, num))
        
#         if len(min_heap) > k:
#             heapq.heappop(min_heap)
        
#     res = [ num for freq, num in min_heap ]
    
#     return nums_map, min_heap, res

# nums = [1,1,1,1,2,2,2,2,3,3,4]
# k = 2

# print(topKFrequent(nums, k))

# Time Complexity O(n log k)
# Space Complexity O(n)

from collections import Counter

def topKFrequent(nums, k):
    
    nums_map = Counter(nums)
    buckets = [[] for num in range(len(nums)+1)]
    
    for num, freq in nums_map.items():
        buckets[freq].append(num)
    
    res = []
    
    for bucket in buckets[::-1]:
        if bucket and len(res) < k:
            for num in bucket:
                if len(res) < k:
                    res.append(num)
       
    return res

nums = [1,1,1,1,2,2,2,2,3,3,4]
k = 2

print(topKFrequent(nums, k))

# Time Complexity O(n)
# Space Complexity O(n)