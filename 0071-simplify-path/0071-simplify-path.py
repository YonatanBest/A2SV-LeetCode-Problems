class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = []
        for i in path:
            if i == "/" and temp:
                if stack and temp == [".", "."]:
                    stack.pop()
                elif len(temp) > 2 or (temp != ["."] and temp != [".", "."]):
                    stack.append("".join(temp))
                temp = []
            elif i != "/":
                temp.append(i)
        if temp:
            if stack and temp == [".", "."]:
                stack.pop()
            elif len(temp) > 2 or (temp != ["."] and temp != [".", "."]):
                stack.append("".join(temp))
        return "/" + "/".join(stack)