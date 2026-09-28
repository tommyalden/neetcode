class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix)

        while low < high:
            mid = (high + low) // 2
            if matrix[mid][-1] < target: low = mid + 1
            else: high = mid

        if low == len(matrix): return False

        row = matrix[low]
        low = 0
        high = len(row)


        # for row in matrix:
        #     if target > row[-1]: continue
                
        #     low = 0
        #     high = len(row)

        while low < high:
            mid = (low + high) // 2

            if row[mid] == target: return True
            elif target < row[mid]: high = mid
            else: low = mid + 1
        
        return False