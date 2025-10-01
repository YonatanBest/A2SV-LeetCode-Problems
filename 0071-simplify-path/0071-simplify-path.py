class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = path.split("/")
        for j in temp:
            if j == "..":
                if stack:
                    stack.pop()
            elif j != "" and j != ".":
                stack.append(j)
        print(stack)
        print(temp)
        return "/" + "/".join(stack)