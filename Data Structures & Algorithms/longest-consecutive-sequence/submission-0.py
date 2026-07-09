class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #input the data into hash table
        #pick 1st element and do if 1stelement+1 in hash increase max by 1 and repeat this for all
        store={}
        currmax=0
        finalmax=0
        for x in nums:
            if x in store:
                store[x]+=1
            else:
                store[x]=1

        for x in store:
            number=x
            currmax=1
            while number+1 in store:
                currmax+=1
                number+=1
            
            if currmax>finalmax:
                finalmax=currmax

        return finalmax