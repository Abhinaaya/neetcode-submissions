class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=[]
        col=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)
        for r in row:
            for j in range(len(matrix[0])):
                matrix[r][j]=0
        for i in range(len(matrix)):
            for c in col:
                matrix[i][c]=0
        



        
        