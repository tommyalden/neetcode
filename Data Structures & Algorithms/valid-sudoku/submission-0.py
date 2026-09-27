class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            found = set()
            for num in row:
                if num == '.': continue
                if num in found: return False
                else: found.add(num)

        for column in range(len(board)):
            found = set()
            for row in range(len(board)):
                num = board[row][column]

                if num == '.': continue
                if num in found: return False
                else: found.add(num)

        for cx in range(1, len(board), 3):
            for cy in range(1, len(board), 3):
                found = set()
                
                for xdiff in range(-1, 2):
                    for ydiff in range(-1, 2):
                        num = board[cy + ydiff][cx + xdiff]

                        if num == '.': continue
                        if num in found: return False
                        else: found.add(num)

        return True