class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length=len(heights)-1
        left=0
        right=length

        max_ever=0
        current_max=0

        while left<right:
            if heights[left]<heights[right]:
                current_max=heights[left]*(right-left)
                max_ever=max(current_max,max_ever)
                left+=1
            else:
                current_max=heights[right]*(right-left)
                max_ever=max(current_max,max_ever)
                right-=1

        return max_ever