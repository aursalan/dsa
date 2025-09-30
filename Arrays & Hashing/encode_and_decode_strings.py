#Encode and Decode Strings

class Solution:
    def encode(self, s):
        parts = []
        
        for string in s:
            parts.append(str(len(string)) + "#" + string[::-1])
               
        return "".join(parts)

    def decode(self, s):
        res = []
        i = 0
    
        while i < len(s):
            j=i
            
            while s[j] != '#':
                j+=1
            
            length = int(s[i:j])
            reversed_string = s[j+1 : j+1+length]
            res.append(reversed_string[::-1])
            i = j+1+length
        
        return res
    

s = ["Hello","World","I Am Crazy"]    

obj = Solution()
encoded = obj.encode(s)
print(encoded)
decoded = obj.decode(encoded)
print(decoded)

# Time Complexity O(n)
# Space Complexity O(n)