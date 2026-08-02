class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seens={}
        seent={}
        if len(s)!=len(t):
            return False

        for x,y in zip(s,t):
            if x in seens:
                seens[x]+=1
            else:
                seens[x]=1
            
            if y in seent:
                seent[y]+=1
            else:
                seent[y]=1

        if seent==seens:
            return True
        else: 
            return False