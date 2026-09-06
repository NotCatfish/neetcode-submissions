class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=nums[0]
        currentsum=nums[0]

        for index in range(1,len(nums)):
            currentsum+=nums[index]
            maxsum=max(currentsum,maxsum)
            if currentsum<0:
                currentsum=0
        
        maxsum=max(maxsum,currentsum)
        return maxsum