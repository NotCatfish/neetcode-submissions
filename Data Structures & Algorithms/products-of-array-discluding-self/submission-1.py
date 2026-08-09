class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[1]*len(nums)
        prefix=1
        suffix=1

        for i in range(len(nums)):
            output[i]*=prefix
            output[len(nums)-1-i]*=suffix
            prefix*=nums[i]
            suffix*=nums[len(nums)-1-i]

        return output