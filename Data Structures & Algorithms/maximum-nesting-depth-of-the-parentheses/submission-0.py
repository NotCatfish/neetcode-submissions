class Solution:
    def maxDepth(self, s: str) -> int:
        maxdepth=0
        currdepth=0
        for value in s:
            if value=="(":
                currdepth+=1
            if value==")":
                currdepth-=1
            maxdepth=max(maxdepth,currdepth)
            
        return maxdepth