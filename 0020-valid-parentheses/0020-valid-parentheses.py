class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for j in s:
            if j == "(" or j == "{" or j == "[":
                stack.append(j)
            elif stack and ((stack[-1] == "[" and j == "]") or (stack[-1] == "{" and j == "}") or (stack[-1] == "(" and j == ")")):
                stack.pop()
            else:
                return False
        return not stack