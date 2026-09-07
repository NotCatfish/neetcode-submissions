class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxStore=0
        while left<right:
            currStore=0
            if heights[left]<heights[right]:
                currStore=heights[left]*(right-left)
                left+=1
            else:
                currStore=heights[right]*(right-left)
                right-=1
            
            maxStore=max(maxStore,currStore)
        
        return maxStore
