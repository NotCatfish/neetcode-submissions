class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1=dict()
        for x in nums:
            if x in dict1:
                dict1[x]+=1
            else:
                dict1[x]=1
        
        for i in dict1:
            if dict1[i]>1 :
                return True

        return False