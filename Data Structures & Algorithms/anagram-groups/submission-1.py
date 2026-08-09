from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen=defaultdict(list)
        for i in strs:
            sorted_word="".join(sorted(i))
            seen[sorted_word].append(i)
        
        return list(seen.values())

