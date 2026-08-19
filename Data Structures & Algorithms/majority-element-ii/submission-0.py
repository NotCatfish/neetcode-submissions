class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        cand1=None
        cand2=None
        count1,count2=0,0
        i=0
        result=[]
        while i<len(nums):
            if cand1==nums[i]:
                count1+=1
            elif cand2==nums[i]:
                count2+=1
            elif count1==0:
                cand1=nums[i]
                count1=1
            elif count2==0:
                cand2=nums[i]
                count2=1
            else:
                count1-=1
                count2-=1
            
            i+=1
        
        count1=0
        count2=0
        for num in nums:
            if num==cand1:
                count1+=1
            elif num==cand2:
                count2+=1

        if count1>len(nums)/3:
            result.append(cand1)
        if count2>len(nums)/3:
            result.append(cand2)
        
        return result