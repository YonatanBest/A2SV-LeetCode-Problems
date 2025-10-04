class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def backtrack(i, j, curr, visited):
            if curr >= len(word):
                return True
            for d in dir:
                i += d[0]
                j += d[1]
                if (i, j) not in visited and i > -1 and j > -1 and i < len(board) and j < len(board[i]) and word[curr] == board[i][j]:
                    visited.add((i, j))
                    curr += 1
                    if backtrack(i, j, curr, visited):
                        return True
                    curr -= 1
                    visited.remove((i, j))
                i -= d[0]
                j -= d[1]
            return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if len(word) == 1 and board[i][j] == word[0]:
                    return True
                if board[i][j] == word[0]:
                    if backtrack(i, j, 1, set([(i, j)])):
                        return True
        return False
