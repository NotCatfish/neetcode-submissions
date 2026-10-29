from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen=defaultdict(list)
        sorted_words=["".join(sorted(w)) for w in strs]

        for index,word in enumerate(sorted_words):
            seen[word].append(strs[index])
        
        return list(seen.values())

