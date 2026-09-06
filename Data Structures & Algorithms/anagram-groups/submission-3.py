from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen=defaultdict(list)
        for word in strs:
            sortedword="".join(sorted(word))
            seen[sortedword].append(word)
        

        return [x for x in seen.values()]