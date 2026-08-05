class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def get_area(ri,ci):
            bag = set()
            bag.add((ri,ci))
            area = 1
            while bag:
                r, c = bag.pop()
                rn = min(r+1, len(grid)-1)
                cn = min(c+1, len(grid[0])-1)
                rp = max(r-1, 0)
                cp = max(c-1, 0)

                for ar, ac in [(rn, c), (rp,c), (r, cn), (r,cp)]:
                    if (ar, ac) not in visited and grid[ar][ac] == 1:
                        bag.add((ar, ac))
                        visited.add((ar,ac))
                        area+=1
            return area

        visited = set()
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c]==1:
                    visited.add((r,c))
                    max_area = max(max_area,get_area(r,c))

        return max_area