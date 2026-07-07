class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps=dict()
        mapt=dict()

        #iterate through s and store in hashmap maps
        for x in s:
            if x in maps:
                maps[x]+=1
            else:
                maps[x]=1
        
        #iterate through t and store in hashmap mapt
        for x in t:
            if x in mapt:
                mapt[x]+=1
            else:
                mapt[x]=1
            
        # if maps and mapt same return true else false
        if maps==mapt:
            return True
        else:
            return False