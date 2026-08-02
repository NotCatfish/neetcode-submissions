import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen={}
        for x in nums:
            if x in seen:
                seen[x]+=1
            else:
                seen[x]=1

        most_frequent=heapq.nlargest(k, seen, key=seen.get)

        return most_frequent