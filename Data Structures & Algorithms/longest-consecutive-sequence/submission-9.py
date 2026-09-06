class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set()
        for num in nums:
            seen.add(num)
        
        maxSeq=0
        for num in seen:
            if num-1 not in seen:
                currSeq=0
                i=0
                while num+i in seen:
                    currSeq+=1
                    i+=1
                
                maxSeq=max(maxSeq,currSeq)
        return maxSeq
