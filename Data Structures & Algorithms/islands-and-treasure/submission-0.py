class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(ri,ci):
            bag = list()
            bag.append((ri, ci))

            while bag:
                r, c = bag.pop(0)
                rn = min(r+1, len(grid)-1)
                cn = min(c+1, len(grid[0])-1)
                rp = max(r-1, 0)
                cp = max(c-1, 0)

                for ar, ac in [(rn, c), (rp,c), (r, cn), (r,cp)]:
                    if grid[ar][ac] > 0:
                        if grid[r][c]+1 < grid[ar][ac]:
                            grid[ar][ac] = grid[r][c]+1
                            bag.append((ar,ac))

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    bfs(r,c)
        
        return