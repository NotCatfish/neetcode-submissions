class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #limits of whole matrix
        lenghtmatrix=len(matrix)-1
        leftmatrix=0
        rightmatrix=lenghtmatrix
        
        #limits of cell of a row
        lenghtcell=len(matrix[0])
        leftcell=0
        rightcell=lenghtcell-1
        

        while leftmatrix<=rightmatrix:

            #finding matrix mid
            midmatrix=leftmatrix+(rightmatrix-leftmatrix)//2   

            #checking if the target is less than 1st element of mid matrix or greater or in the range of the middle matrix
            if target>matrix[midmatrix][rightcell]:
                leftmatrix=midmatrix+1
                continue
            elif target<matrix[midmatrix][0]:
                rightmatrix=midmatrix-1

            else:
                #when its in range of middle matrix perform binary searh on the cell of mid matrix
                while leftcell<=rightcell:
                    midcell=leftcell+(rightcell-leftcell)//2
                    if matrix[midmatrix][midcell]==target:
                        return True
                    elif target<matrix[midmatrix][midcell]:
                        rightcell=midcell-1
                    elif target>matrix[midmatrix][midcell]:
                        leftcell=midcell+1
                    else:
                        return False
                    

            
        return False
