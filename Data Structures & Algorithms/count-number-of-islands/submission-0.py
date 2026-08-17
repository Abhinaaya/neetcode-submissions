class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        def dfs(r,c):
            if (0>r or r>=m or c<0 or c>=n or grid[r][c]=='0' or (r,c) in visited):
                return False
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        count=0
        for row in range(m):
            for col in range(n):
                if grid[row][col]=='1' and (row,col) not in visited:
                    count+=1
                    dfs(row,col)
        return count
        
