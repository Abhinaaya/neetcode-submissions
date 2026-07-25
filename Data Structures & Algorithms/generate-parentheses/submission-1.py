class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        
        def dfs(curr,open_c,close_c):
            if len(curr)==2*n:
                ans.append(curr)
                return
            if open_c<n:
                dfs(curr+"(",open_c+1,close_c)
            if open_c>close_c:
                dfs(curr+")",open_c,close_c+1)
        dfs("",0,0)
        return ans
        