class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
            
        intervals.sort()
        prevEnd = intervals[0][1]
        i = 1
        res = 0 
        
        while i < len(intervals):
            if prevEnd <= intervals[i][0]:
                prevEnd = intervals[i][1]
            else:
                res += 1  
                prevEnd = min(prevEnd, intervals[i][1])
            
            i += 1 
            
        return res 