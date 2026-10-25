class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        res = 1e3

        while left<=right:
            mid = (left + right)//2
            res = min(nums[mid],res)
            if nums[mid] < nums[right]:
                right = mid - 1
            else: 
                left = mid+1
            
        return res

            