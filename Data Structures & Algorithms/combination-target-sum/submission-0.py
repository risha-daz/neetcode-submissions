class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        def f(nums, k, ind, res):
            if k==0: return [res]
            if ind>len(nums)-1 or k<0 or nums[ind]>k: return []
            # left: add 1 from index ind and subtract from k
            l = f(nums, k-nums[ind], ind, res + [nums[ind]])

            # right: none from index ind and use same k
            r = f(nums, k, ind+1, res)
 
            return l+r

        return f(nums, target, 0, [])