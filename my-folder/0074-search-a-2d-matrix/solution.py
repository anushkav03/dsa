class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # def searchRow(matrix, target_row, target):
        #     if target in matrix[target_row]:
        #         return True
        #     else:
        #         return False

        # if len(matrix) == 1:
        #     return searchRow(matrix, 0, target)

        # left = 0
        # right = len(matrix)
        # target_row = None
        # while left < right:
        #     curr = math.ceil((right - left) / 2)
        #     if target == matrix[curr][0]:
        #         return True
        #     elif target < matrix[curr][0]:
        #         # look in bottom half
        #         if target >= matrix[curr - 1][0]:
        #             # search row curr - 1
        #             target_row = curr - 1
        #             return searchRow(matrix, target_row, target)
        #         else:
        #             # adjust right ptr
        #             right = curr - 1
        #     else:
        #         # look in top half
        #         # if this is last row, or target is btw curr and next row
        #         if curr == len(matrix) - 1 or target < matrix[curr + 1][0]:
        #             # search row curr
        #             target_row = curr
        #             return searchRow(matrix, target_row, target)
        #         else:
        #             # adjust bottom ptr
        #             left = curr + 1
        # return False
        r, c = 0, len(matrix[0]) - 1
        while r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[0]):
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False
        
        
