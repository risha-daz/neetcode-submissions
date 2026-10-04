class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr_min = prices[0]
        for i in prices:
            res = max(i-curr_min, res)
            curr_min = min(i,curr_min)
        return res
