class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=0
        left=0
        right=1
        while right<len(s):
            ans+=abs(ord(s[right])-ord(s[left]))
            right+=1
            left+=1
        
        
        return ans