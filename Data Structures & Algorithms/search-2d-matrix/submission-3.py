class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target > row[-1]: continue
                
            low = 0
            high = len(row)

            while low < high:
                midpoint = (low + high) // 2

                if row[midpoint] == target: return True
                elif target < row[midpoint]: high = midpoint
                else: low = midpoint + 1

            return False
        return False