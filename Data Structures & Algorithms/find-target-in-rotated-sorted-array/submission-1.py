class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        def f(a,b,n):
            return n>=a and n<=b

        while left <= right:
            mid = (left + right) // 2
            nl = nums[left]
            nr = nums[right]
            nm = nums[mid]
            if nm == target: return mid
            if (nl < nm and f(nl,nm,target) or 
                nm < nr and not f(nm,nr,target)):
                right = mid - 1
            else: left = mid + 1
        return -1