class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        
        res = [[0]*COLS for _ in range(ROWS)]
        ret = []

        def traverse(ri,ci, n):
            if res[ri][ci] >= n: return
            bag = list()
            bag.append((ri,ci))
            res[ri][ci] += n

            while bag:
                r, c = bag.pop()
                directions = [(r+1, c), (r-1, c), (r, c+1), (r,c-1)]

                for ar, ac in directions:
                    if (
                        0 <= ar < ROWS and
                        0 <= ac < COLS and
                        res[ar][ac] < n and
                        heights[ar][ac] >= heights[r][c]
                    ):
                        res[ar][ac] += n
                        bag.append((ar,ac))

        for r in range(ROWS):
            traverse(r,0, 1)

        for c in range(COLS):
            traverse(0,c, 1)

        for r in range(ROWS):
            traverse(r,COLS-1, 2)

        for c in range(COLS):
            traverse(ROWS-1,c, 2)
        
        for i in range(ROWS):
            for j in range(COLS):
                if res[i][j] == 3:
                    ret.append([i,j])
        return ret


        

