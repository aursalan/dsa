#Contains Duplicate 

# li = [1,2,3,1]

# res = False;
# for i in range(len(li)):
#     curr = li[i]
#     for j in li[i+1:]:
#         if curr == j:
# 			res = True;
# 			break;
# 	if(res==True):
# 		break;
# print(res)

#Time Complexity O(n)
#Space Complexity O(1)

# li = [1,2,3,1]
# s = set()
# res = False

# for i in li:
#     if( i in s):
#         res = True
#         break
#     else:
#         s.add(i)
# print(res)

# Time Complexity O(n)
# Space Complexity O(n)

li = [1,2,3,1]
res = True if len(li) != len(set(li)) else False
print(res)