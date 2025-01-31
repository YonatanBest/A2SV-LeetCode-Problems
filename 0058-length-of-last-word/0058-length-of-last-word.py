class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        check = False
        num = 0
        for i in reversed(s):
            if i.isalnum():
                check = True
                num += 1
            if not i.isalnum() and check:
                return num
        return num