class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        if numRows == 1:
            return result
            
        result.append([1, 1])
        if numRows == 2:
            return result
        
        for i in range(3, numRows + 1):
            temp = [1]

            prev_row = result[-1] 
            
            for j in range(1, i - 1):

                temp.append(prev_row[j - 1] + prev_row[j]) 
                
            temp.append(1)
            result.append(temp)
        
        return result