class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
               stack.append([char, 1])
               
        final_str = []

        for j in stack:
            final_str.extend([j[0]]*j[1])

        return "".join(final_str)