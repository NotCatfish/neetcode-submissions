class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        length=len(s)
        longest_len=0
        substring=[]
        if length==1:
            return 1
        while right<length:
            if s[right] in substring:
                
                left=right
                substring=[]
                substring.append(s[right])
            else:
                substring.append(s[right])
            
            right+=1
            longest_len=max(longest_len,len(substring))
        
        return longest_len
