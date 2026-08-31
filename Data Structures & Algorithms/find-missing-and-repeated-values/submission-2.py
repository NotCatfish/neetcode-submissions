from collections import defaultdict
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen=defaultdict(set)
        for row in grid:
            for column in row:
                if column in seen[1]:
                    seen[2].add(column)
                else:
                    seen[1].add(column)
                
        return [int(list(seen[2])[0]),int(next(x for x in range(1,len(grid) * len(grid[0])+1) if x not in seen[1]))]