"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start=[]
        end=[]

        for i in intervals:
            start.append(int(i.start))
            end.append(int(i.end))
        
        start.sort()
        end.sort()

        maxneed=0
        s=0
        e=0
        if len(intervals)==1:
            return 1
        count=0
        while s<len(start):
            if start[s]<end[e]:
                count+=1
                s+=1
            else:
                e+=1
                count-=1
            maxneed=max(maxneed,count)
        
        return maxneed
            


