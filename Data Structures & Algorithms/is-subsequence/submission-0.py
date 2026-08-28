class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        main=0
        sub=0
        while main<len(t) and sub<len(s):
            if s[sub]==t[main]:
                sub+=1
            main+=1
        
        if sub==len(s):
            return True
        else:
            return False