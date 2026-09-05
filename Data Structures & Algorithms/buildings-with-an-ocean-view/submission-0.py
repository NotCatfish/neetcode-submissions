class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxheight=0
        length=len(heights)-1
        result=[]

        for index in range(length,-1,-1):
            if maxheight<heights[index]:
                result.append(index)
            maxheight=max(maxheight,heights[index])

        result.sort()
    
        return result