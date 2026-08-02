from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)

        for key in strs:
            sorted_word="".join(sorted(key))
            anagrams[sorted_word].append(key)

        return list(anagrams.values())
        