class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mins=min(strs)
        maxs=max(strs)
        prefix=""
        for i in range(len(mins)):
            if mins[i]==maxs[i]:
                prefix+=mins[i]
            else:
                return prefix
        
        return prefix