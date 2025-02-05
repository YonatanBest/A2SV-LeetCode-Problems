# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        answer = []
        mlc = False
        for line in source:
            if not mlc:
                temp = []

            i = 0
            while i < len(line):
                if mlc:
                    if line[i:i+2] == "*/":
                        mlc = False
                        i += 1
                else:
                    if line[i:i+2] == "/*":
                        mlc = True
                        i += 1
                    elif line[i:i+2] == "//":
                        break
                    else:
                        temp.append(line[i])
                
                i += 1

            if not mlc and temp:
                answer.append("".join(temp))

        return answer