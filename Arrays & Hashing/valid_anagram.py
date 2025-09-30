#Valid Anagram 

# def is_anagram(s,t):
    
#     if len(s) != len(t):
#         return False
    
#     counts = {}
    
#     for char in s:
#         counts[char] = counts.get(char,0) + 1

#     for char in t:
#         if char not in counts or counts[char] == 0:
#             return False
#         counts[char] -=1

#     return True

# print(is_anagram('rat','rtt'))

# Time Complexity O(n)
# Space Complexity O(n) 

from collections import Counter

s = "rat"
t = "car"

res = True if Counter(s)==Counter(t) else False

print(res)

# Time Complexity O(n)
# Space Complexity O(n) 