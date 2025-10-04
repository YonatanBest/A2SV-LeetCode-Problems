class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def valid(path):
            stack = []
            for i in path:
                if i == "(":
                    stack.append(i)
                elif stack:
                    stack.pop()
                else:
                    return False
            return not stack
        def backtrack(path):
            nonlocal ans
            if len(path) == n * 2:
                if valid(path.copy()):
                    ans.append("".join(path.copy()))
                return
            for j in ["(", ")"]:
                path.append(j)
                backtrack(path)
                path.pop()
            return
        backtrack([])
        return ans