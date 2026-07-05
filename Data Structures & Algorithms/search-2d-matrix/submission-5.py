class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                #Run another binary search
                l, r = 0, COLS - 1
                while l <= r:
                    middle = (l + r) // 2
                    if matrix[m][middle] == target:
                        return True
                    elif matrix[m][middle] > target:
                        r -= 1
                    else:
                        l+=1
                break
            elif target > matrix[m][-1]:
                l+=1
            else:
                r -= 1
        return False