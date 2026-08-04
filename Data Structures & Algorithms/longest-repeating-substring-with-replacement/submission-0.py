from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        seen=defaultdict(int)
        max_len=0

        for right in range(len(s)):
            seen[s[right]]+=1
            windowLen=right-left+1
            maxFreq=max(seen.values())

            while windowLen-maxFreq>k:
                seen[s[left]]-=1
                left+=1
                windowLen=right-left+1

            max_len=max(max_len,right-left+1)

        return max_len