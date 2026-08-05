class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        edge = [[False]*COLS for _ in range(ROWS)]

        def capture_list(ri, ci):
            bag = list()
            bag.append((ri,ci))

            while bag:
                r,c = bag.pop()
                for ar, ac in [(r+1, c), (r-1,c), (r, c+1), (r,c-1)]:
                    if (0 <= ar < len(board) and
                        0 <= ac < len(board[0]) and
                        board[ar][ac] == 'O' and
                        not edge[ar][ac]):
                            edge[ar][ac] = True
                            bag.append((ar,ac))

        for r in [0, ROWS-1]:
            for c in range(COLS):
                if board[r][c] == 'O' and not edge[r][c]:
                    edge[r][c] = True
                    capture_list(r,c)
        for c in [0, COLS-1]:
            for r in range(ROWS):
                if board[r][c] == 'O' and not edge[r][c]:
                    edge[r][c] = True
                    capture_list(r,c)
        
        
        for r in range(ROWS-1):
            for c in range(COLS-1):
                if not edge[r][c]:
                    board[r][c] = 'X'
                    


            