# Group Anagrams

# from collections import Counter

# li = ["eat","tea","tan","ate","nat","bat"]
# res = []
# visited = [False for i in range(len(li))]

# length = len(li)

# for i in range(length):
#     temp = []
#     if visited[i] == False:
#         temp.append(li[i])
#         visited[i] = True
    
#     for j in range(i+1, length):
#         if visited[j] == False and Counter(li[i]) == Counter(li[j]):
#             temp.append(li[j])
#             visited[j]=True
#     if temp:
#         res.append(temp)

# print(res)

# Time Complexity O(n^2 . k)
# Space Complexity O(n . k)

from collections import defaultdict

def groupAnagrams(strs):
    
    anagram_groups = defaultdict(list)
    
    for word in strs:
        sorted_word = "".join(sorted(word))
        
        anagram_groups[sorted_word].append(word)
        
    return list(anagram_groups.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))

# Time Complexity O(n . k log k)
# Space Complexity O(n . k)