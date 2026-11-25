class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, ind):
            if ind==len(word):
                return True
            if r<0 or c<0 or r>= ROWS or c >= COLS:
                return False
            if board[r][c] == word[ind]:
                temp = board[r][c]
                board[r][c] = '#'
                found = (dfs(r+1, c, ind+1) or
                        dfs(r-1, c, ind+1) or
                        dfs(r, c+1, ind+1) or
                        dfs(r, c-1, ind+1))
                if found: return True
                else: board[r][c] = temp
            
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0): return True
        return False
                