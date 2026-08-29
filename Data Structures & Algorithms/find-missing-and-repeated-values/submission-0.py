class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total_elements = n * n
        
        # 1. Start from 1, go up to total_elements (inclusive)
        seen = {i: 0 for i in range(1, total_elements + 1)}
        ans = []
        
        for row in grid:
            for num in row:
                seen[num] += 1
                if seen[num] == 2:
                    # 2. Append the number itself, not its frequency
                    ans.append(num) 
                    
        for key, value in seen.items():
            if value == 0:
                # 3. Append the key, because the key is the missing number
                ans.append(key) 
                break
                
        return ans