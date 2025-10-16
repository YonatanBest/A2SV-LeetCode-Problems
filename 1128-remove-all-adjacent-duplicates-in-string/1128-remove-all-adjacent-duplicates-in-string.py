class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for j in s:
            if not stack:
                stack.append(j)
            elif stack[-1] == j:
                stack.pop()
            else:
                stack.append(j)

        return "".join(stack)