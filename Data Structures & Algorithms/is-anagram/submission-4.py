from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        seens=defaultdict(int)
        seent=defaultdict(int)
        for i in range(len(s)):
            seens[s[i]]+=1
            seent[t[i]]+=1
        
        if seens==seent:
            return True
        else:
            return False