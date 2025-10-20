class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for j in s:
            if j != "]":
                stack.append(j)
            else:
                temp = []
                while stack[-1] != "[":
                    temp.append(stack.pop())

                stack.pop()

                times = []
                while stack and stack[-1].isdigit():
                    times.append(stack.pop())
                num = int("".join(times)[::-1]) 
                stack.append("".join(temp[::-1]) * num)

        return "".join(stack)