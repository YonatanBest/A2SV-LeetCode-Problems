from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in box[i//3, j//3] or board[i][j] in row[i] or board[i][j] in col[j]:
                    return False
                else:
                    box[i//3, j//3].add(board[i][j])
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
        return True