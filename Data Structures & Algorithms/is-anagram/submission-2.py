from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict=defaultdict(int)
        tdict=defaultdict(int)

        for key in s:
            sdict[key]+=1
        for key in t:
            tdict[key]+=1

        if sdict==tdict:
            return True
        
        return False