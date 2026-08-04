from collections import defaultdict
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        seen=defaultdict(int)
        left=0
        answer=[]
        for right in range(len(nums)):
            seen[nums[right]]+=1

            if right-left+1>=k:
                answer.append(max(seen))
                seen[nums[left]]-=1
                if seen[nums[left]]==0:
                    del seen[nums[left]]
                left+=1

        return answer
        
