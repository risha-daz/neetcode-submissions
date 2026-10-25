import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = []

        def f(piles, k):
            res = 0
            for i in piles:
                res += math.ceil(i/k)
            return res
        
        while left <= right:
            mid = (left + right) // 2
            h_ = f(piles, mid)
            if h_ <= h: res.append(mid)
            if h_ > h: left = mid+1
            else: right = mid-1

        return min(res)
