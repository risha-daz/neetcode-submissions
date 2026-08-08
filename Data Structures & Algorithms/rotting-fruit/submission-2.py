class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = {} # cell : step number
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0

        def bfs(ri,ci):
            visited[(ri,ci)] = 0
            bag = list()
            bag.append((ri,ci))

            while bag:
                r, c = bag.pop(0)
                dist = visited[(r,c)]
                directions = [(r+1, c), (r-1, c), (r, c-1), (r, c+1)]

                for ar, ac in directions:
                    if (
                        0 <= ar < ROWS and
                        0 <= ac < COLS and
                        grid[ar][ac] > 0 
                    ):
                        if grid[ar][ac] == 1:
                            bag.append((ar,ac))
                            visited[(ar, ac)] = dist+1
                            grid[ar][ac] = 2
                        else:
                            if (ar,ac) in visited and visited[(ar,ac)] > dist+1:
                                bag.append((ar,ac))
                                visited[(ar, ac)] = dist+1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2 and (r,c) not in visited:
                    bfs(r,c)
        print(visited)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        return max(list(visited.values())+[0])

