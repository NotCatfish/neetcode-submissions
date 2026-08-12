class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        rightmax=height[len(height)-1]
        leftmax=height[0]
        storage=0
        left=0
        right=len(height)-1
        while left<right:
            if height[left]<height[right]:
                leftmax=max(leftmax,height[left])
                storage+=leftmax-height[left]
                left+=1
                
            else:
                rightmax=max(rightmax,height[right])
                storage+=rightmax-height[right]
                right-=1
                

        return storage