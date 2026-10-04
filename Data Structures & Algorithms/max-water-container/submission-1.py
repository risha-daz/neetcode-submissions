class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights)-1
        while l<r:
            vol = (r-l)*min(heights[l],heights[r])
            res=max(res, vol)
            if heights[l]<heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            else:
                if heights[r-1] > heights[l+1]:
                    r-=1
                else:
                    l+=1
        return res
