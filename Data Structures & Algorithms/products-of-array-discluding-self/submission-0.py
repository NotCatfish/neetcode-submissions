class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenght=len(nums)
        prefix_sum=[]
        suffix_sum=[]
        result=[0]*lenght
        prefix=1
        suffix=1
        for x in range(lenght):
            prefix_sum.append(prefix)
            prefix*=nums[x]
            suffix_sum.append(suffix)
            suffix*=nums[lenght-x-1]

        for x in range(lenght):
            result[x]=suffix_sum[lenght-x-1]*prefix_sum[x]
        
        return result