class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result=0
        i=0
        n=len(mat)
        while i < n:
            if i+i==i+n-1-i:
                result+=mat[i][i]
            else:
                result+=mat[i][n-i-1]
                result+=mat[i][i]
            i+=1
        
        return result