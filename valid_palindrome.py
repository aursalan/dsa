# Valid Palindrome

# class Solution(object):
#     def isPalindrome(self, s):
#         temp = ""
        
#         for char in s:
#             if (65 <=  ord(char) <= 90 ) or ( 97 <= ord(char) <= 122 ) or (48 <= ord(char) <=57):
#                 temp += char
        
#         temp = temp.lower()
#         reversed_temp = "".join(reversed(temp))
#         return temp == reversed_temp
            
# s = " "
# obj = Solution()
# print(obj.isPalindrome(s))

# Time Complexty O(n)
# Space Complexity O(n)

class Solution(object):
    def isPalindrome(self, s):
    
        i = 0
        j = len(s)-1
        
        while i<j:
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i+=1
                    j-=1
        return True

s = "A man, a plan, a canal: Panama"
obj = Solution()
print(obj.isPalindrome(s))

# Time Complexty O(n)
# Space Complexity O(1)