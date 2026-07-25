class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows=len(board)
        Cols=len(board[0])
        def dfs(index,r,c):
            if len(word)==index:
                return True
            if (r<0 or r>=Rows or c<0 or c>=Cols or word[index]!=board[r][c]):
                return False
            temp=board[r][c]
            board[r][c]="#"
            found=(dfs(index+1,r+1,c)or dfs(index+1,r-1,c) or dfs(index+1,r,c+1) or dfs(index+1,r,c-1))
            board[r][c]=temp
            return found
        for r in range(Rows):
            for c in range(Cols):
                if dfs(0,r,c):
                    return True
        return False


        