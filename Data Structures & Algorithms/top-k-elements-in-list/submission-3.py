from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countdict=defaultdict(int)
        freqdict=defaultdict(list)

        for num in nums:
            countdict[num]+=1
        

        for num,freq in countdict.items():
            freqdict[freq].append(num)
        
        sorted_keys =sorted(freqdict.keys(), reverse=True)

        count=0
        result=[]
        for freq in sorted_keys:
            if len(result)<k:
                result.extend(freqdict[freq])
            else:
                break
            
        return result