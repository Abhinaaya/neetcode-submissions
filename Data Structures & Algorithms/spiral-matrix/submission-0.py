class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t=0
        b=len(matrix)-1
        l=0
        r=len(matrix[0])-1
        ans=[]
        while l<=r and t<=b:
            for j in range(l,r+1):
                ans.append(matrix[t][j])
            t+=1
            for i in range(t,b+1):
                ans.append(matrix[i][r])
            r-=1
            if t<=b:
                for j in range(r,l-1,-1):
                    ans.append(matrix[b][j])
                b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    ans.append(matrix[i][l])
                l+=1
        return ans

                
                

        