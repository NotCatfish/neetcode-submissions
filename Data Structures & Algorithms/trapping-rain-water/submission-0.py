class Solution:
    def trap(self, height: List[int]) -> int:
        length=len(height)

        left=0
        right=length-1
        water=0
        left_max=height[left]
        right_max=height[right]

        while left<right:
            if height[left]<height[right]:
                left+=1
                left_max=max(left_max,height[left])
                water+=left_max-height[left]
            
            else:
                right-=1
                right_max=max(right_max,height[right])
                water+=right_max-height[right]
            
        return water
                