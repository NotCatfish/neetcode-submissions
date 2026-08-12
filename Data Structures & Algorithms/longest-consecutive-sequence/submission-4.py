class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0
        for right in nums:
            if right-1 not in nums:
                currLong=1
                while right+1 in nums:
                    currLong+=1
                    right=right+1
                
                longest=max(longest,currLong)
        
        return longest