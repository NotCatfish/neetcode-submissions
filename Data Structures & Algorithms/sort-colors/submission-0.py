class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=-1
        right=len(nums)
        index=0
        while index<right:
            if nums[index]==0:
                left+=1
                nums[left],nums[index]=nums[index],nums[left]
                index+=1
            elif nums[index]==1:
                index+=1
            elif nums[index]==2:
                right-=1
                nums[right],nums[index]=nums[index],nums[right]
