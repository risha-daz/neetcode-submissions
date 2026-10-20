from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0 for _ in range(len(temperatures))]
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0]<t:
                val, ind = stack.pop()
                res[ind] = i - ind
            stack.append((t,i))
        return res




