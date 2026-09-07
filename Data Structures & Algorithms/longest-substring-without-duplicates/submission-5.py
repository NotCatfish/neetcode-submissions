class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        maxLen=0
        left=0
        right=0
        currLen=0
        while right< len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
                currLen-=1
            
            seen.add(s[right])
            right+=1
            currLen+=1
        
            maxLen=max(maxLen,currLen)
        
        return maxLen