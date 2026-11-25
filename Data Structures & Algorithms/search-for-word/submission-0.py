class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, ind):
            if ind==len(word):
                return True
            if r<0 or c<0 or r>= ROWS or c >= COLS:
                return False
            if (r,c) not in visited and board[r][c] == word[ind]:
                visited.add((r,c))
                found = (dfs(r+1, c, ind+1) or
                        dfs(r-1, c, ind+1) or
                        dfs(r, c+1, ind+1) or
                        dfs(r, c-1, ind+1))
                if found: return True
                else: visited.remove((r,c))
            
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0): return True
        return False
                