class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=len(s)
        left=0
        right=0
        maxLen=0
        seen=list()
        while right<length:
            if s[right] not in seen:
                seen.append(s[right])
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
                    curr_len=0
                seen.append(s[right])
            maxLen=max(maxLen,len(seen))
            right+=1

        return maxLen
            

            
