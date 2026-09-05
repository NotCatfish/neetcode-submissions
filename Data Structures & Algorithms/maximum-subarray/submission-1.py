class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        currentsum=nums[0]

        for index in range(1,len(nums)):
            currentsum = max(nums[index], currentsum + nums[index])
            maxsum = max(maxsum, currentsum)
        
        maxsum=max(maxsum,currentsum)
        return maxsum