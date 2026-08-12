class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=set()
        longest=0
        left=0
        currlen=0
        if not s:
            return 0
        for right in range(len(s)):
            if s[right] in result:
                while s[right] in result:
                    result.remove(s[left])
                    currlen-=1
                    left+=1
                result.add(s[right])
                currlen+=1
            else:
                result.add(s[right])
                currlen+=1
            
            longest=max(longest,currlen)
        
        return longest