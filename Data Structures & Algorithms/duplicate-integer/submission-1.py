class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}

        for index,value in enumerate(nums):
            if value in seen:
                return True
            else:
                seen[value]=index

        return False