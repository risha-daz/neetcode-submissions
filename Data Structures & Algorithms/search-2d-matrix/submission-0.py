class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        m = len(matrix) # rows
        n = len(matrix[0]) # cols
        right = n*m - 1

        # index[i,j] = i + n*j

        while left <= right:
            mid = (left + right) // 2
            j = mid%n
            i = mid//n

            if matrix[i][j] == target: return True
            if matrix[i][j] < target: left = mid+1
            else: right = mid-1

        return False
