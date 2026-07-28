from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t = Counter(t)
        maxChar = len(t)
        minLength = float('inf')
        substring = ""
        left, right, matched, freq = 0,0,0, {}

        while right<len(s):

            while right<len(s) and matched != maxChar:
                
                freq[s[right]] = freq.get(s[right],0) + 1  
                if s[right] in t:
                    if freq[s[right]] == t[s[right]]:
                        matched+=1 
                right+=1
                
            while matched == maxChar:

                currentLength = right - left

                if currentLength < minLength:
                    minLength = currentLength
                    substring = s[left:right]

                if s[left] not in t:
                    freq[s[left]] -=1
                    left+=1

                else:
                    freq[s[left]] -=1
                    if freq[s[left]] < t[s[left]]:
                        matched-=1
                    left+=1

        return substring