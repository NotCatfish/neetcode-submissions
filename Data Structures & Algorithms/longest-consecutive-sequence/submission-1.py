class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen={}
        lenght=len(nums)
        current_len=1
        max_len=1
        if lenght==0:
            return 0
        for x in nums:
            if x in seen:
                seen[x]+=1
            else:
                seen[x]=1

        for key in seen:
            if key-1 not in seen:
                current_len=1
                current_key=key
                while current_key+1 in seen:
                    current_len+=1
                    current_key+=1
                    key+=1

                if current_len>max_len:
                    max_len=current_len

        return max_len

