class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for right in range(len(nums)):
            complement=target-nums[right]
            if complement in seen:
                return [seen[complement],right]
            else:
                seen[nums[right]]=right
        
