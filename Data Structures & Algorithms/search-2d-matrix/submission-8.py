class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS - 1
        while l <= r:
            m = (l + r) // 2
            if target >= matrix[m][0] and target <= matrix[m][-1]:
                #Start second binary search
                print('here')
                left, right = 0, COLS - 1
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[m][mid] == target:
                        return True
                    elif matrix[m][mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
                return False
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        
        return False 