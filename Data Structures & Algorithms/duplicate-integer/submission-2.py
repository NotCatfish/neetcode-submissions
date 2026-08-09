class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length=len(nums)
        nums=set(nums)

        if length==len(nums):
            return False
        else:
            return True

            
