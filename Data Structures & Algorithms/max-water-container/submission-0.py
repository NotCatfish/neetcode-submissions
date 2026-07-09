class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lenght=len(heights)
        left=0
        right=lenght-1
        finalmax=0
        currmax=0
        while left<right:
            if heights[left]<=heights[right]:
                currmax=heights[left]*(right-left)
                left+=1
            else:
                currmax=heights[right]*(right-left)
                right-=1
            
            if finalmax<currmax:
                finalmax=currmax
            
        return finalmax