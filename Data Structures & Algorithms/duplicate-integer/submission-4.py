class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for x in range(0,len(nums)):
            if nums[x]==nums[x-1]:
                return True

        
        return False
            
