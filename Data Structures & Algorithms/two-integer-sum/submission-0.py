class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(nums)):
            a = nums[i]
            if a in mem.keys(): return [mem[a], i]
            else: mem[target - a] = i
        return [0,0]