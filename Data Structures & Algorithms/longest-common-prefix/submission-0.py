class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first,last=strs[0],strs[-1]
        i=0
        longest=""
        while last[i]==first[i]:
            longest+=first[i]
            i+=1
        
        return longest