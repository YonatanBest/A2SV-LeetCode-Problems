class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        check = False
        num = 0
        for i in reversed(s):
            if i != " ":
                check = True
                num += 1
            if i == " " and check:
                return num
        return num