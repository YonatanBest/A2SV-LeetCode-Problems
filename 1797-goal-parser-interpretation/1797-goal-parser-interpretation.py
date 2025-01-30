class Solution:
    def interpret(self, command: str) -> str:
        final = []
        temp = []
        for i in range(len(command)):
            if command[i] == "G":
                final.append("G")
            else:
                temp.append(command[i])
                if temp == ["(", ")"]:
                    final.append("o")
                    temp = []
                elif temp == ["(", "a", "l", ")"]:
                    final.append("al")
                    temp = []
                else:
                    pass
        return "".join(final)