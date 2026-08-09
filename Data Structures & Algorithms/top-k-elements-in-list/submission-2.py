from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen=defaultdict(int)
        answer=[]
        for x in nums:
            seen[x]+=1
        
        frequency=[[] for x in range(len(nums)+1)]
        for key,value in seen.items():
            frequency[value].append(key)

        for i in range(len(frequency)-1,-1,-1):
            for n in frequency[i]:
                answer.append(n)
            
            if len(answer)==k:
                return answer