class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = {}

        left, right, maxLength, maxFreq = 0,0,0,0

        while right<len(s):

            if s[right] not in freq.keys():
                freq[s[right]]=1
            else:
                freq[s[right]]+=1
            
            maxFreq = max(freq[s[right]], maxFreq)

            if maxFreq+k >= right-left+1:
                maxLength = right-left+1
                right+=1
            
            else:
                freq[s[left]]-=1
                left+=1
                right+=1
        
        return maxLength



        