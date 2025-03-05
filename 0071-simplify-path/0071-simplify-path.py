class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = list(map(str, path.split("/")))
        stack = []
        for i in arr:
            if i == "." or i == "":
                pass
            elif stack and i == "..":
                stack.pop()
            elif i != "..":
                stack.append(i)
        return "/" + "/".join(stack)