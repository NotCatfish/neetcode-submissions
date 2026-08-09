class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        output=[1]*length
        prefix=1
        suffix=1

        for i in range(length):
            output[i]*=prefix
            output[length-1-i]*=suffix
            prefix*=nums[i]
            suffix*=nums[length-1-i]

        return output