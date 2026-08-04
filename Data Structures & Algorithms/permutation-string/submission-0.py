from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1dict=defaultdict(int)
        s2dict=defaultdict(int)
        left=0
        s1len=len(s1)
        for x in s1:
            s1dict[x]+=1

        for right in range(len(s2)):
            s2dict[s2[right]]+=1

            if right-left+1>s1len:
                s2dict[s2[left]]-=1
                if s2dict[s2[left]]==0:
                    del s2dict[s2[left]]
                left+=1

            if s1dict==s2dict:
                return True
            

        return False

        