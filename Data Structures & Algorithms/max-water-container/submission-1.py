class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        answer=0
        while left<right:
            currMax=0
            if heights[left]>=heights[right]:
                currMax=heights[right]*(right-left)
                right-=1
            else:
                currMax=heights[left]*(right-left)
                left+=1
            
            answer=max(answer,currMax)
        
        return answer