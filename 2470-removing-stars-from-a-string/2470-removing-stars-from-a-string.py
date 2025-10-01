class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for j in s:
            if j == "*" and stack:
                stack.pop()
            else:
                stack.append(j)

        return "".join(stack)