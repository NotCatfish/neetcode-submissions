class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixSum=[1]
        suffixSum=[1]
        psum=1
        ssum=1
        
        for i in range(len(nums)-1):
            ssum*=nums[len(nums)-i-1]
            psum*=nums[i]
            suffixSum.append(ssum)
            prefixSum.append(psum)
        suffixSum.reverse()

        return [a*b for a,b in zip(prefixSum,suffixSum)]