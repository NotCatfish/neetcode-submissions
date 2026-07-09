class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store={}
        
        for x in nums:
            if x in store:
                store[x]+=1
            else:
                store[x]=1

        unique_elements = list(store.keys())
        unique_elements.sort(key=lambda x: store[x], reverse=True)
        top = unique_elements[:k]

        return top
