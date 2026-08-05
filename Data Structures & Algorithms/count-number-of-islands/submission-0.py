class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def mark_visited(ri,ci):
            bag = set()
            bag.add((ri,ci))
            while bag:
                (r,c) = bag.pop()
                rn = min(len(grid)-1,r+1)
                cn = min(len(grid[0])-1,c+1)
                rp = max(0,r-1)
                cp = max(0,c-1)

                for ar, ac in [(r,cn), (r,cp), (rn,c), (rp,c)]:
                    if (ar, ac) not in visited and grid[ar][ac] == '1':
                        visited.add((ar,ac))
                        bag.add((ar,ac))
        count = 0
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c]=='1':
                    count+=1
                    mark_visited(r,c)

        return count