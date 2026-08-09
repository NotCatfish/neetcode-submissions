from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=defaultdict(int)

        for index in range(len(nums)):
            complement=target-nums[index]
            if complement in seen:
                return [seen[complement],index]
            seen[nums[index]]=index