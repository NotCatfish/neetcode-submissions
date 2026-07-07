class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #iterate and store index as key and then store dict as value which has alphabet as key and count as value
        dictionary={}
        for x in strs:
            sortedstr="".join(sorted(x))
            if sortedstr in dictionary:
                dictionary[sortedstr].append(x)
            else:
                dictionary[sortedstr]=[]
                dictionary[sortedstr].append(x)

        return list(dictionary.values())