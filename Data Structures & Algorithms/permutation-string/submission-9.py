from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2)<len(s1):
            return False
        
        left, right, freq = 0,0, {} 
        lens1 = len(s1)
        s1 = Counter(s1)

        while right<lens1:

            if s2[right] not in freq.keys():
                freq[s2[right]] = 1
                right+=1
            else:
                freq[s2[right]] += 1
                right+=1

        while right<=len(s2):

            if right-left == lens1:
                if freq == s1:
                    print("Freq: ", freq)
                    print("S1: ", s1)
                    return True

                else:
                    freq[s2[left]]-=1 

                    if freq[s2[left]] == 0:
                        del freq[s2[left]]

                    left+=1

                    if right<len(s2): 
                        if s2[right] not in freq.keys():
                            freq[s2[right]] = 1

                        else:
                            freq[s2[right]] += 1

                    right+=1
        
        return False