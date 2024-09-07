class Solution:
    def isPalindrome(self, x: int) -> bool:
        # i = 0
        # j = len(str(x)) - 1
        # value = True
        # while i < j:
        #     if str(x)[i] != str(x)[j]:
        #         value = False
        #     i += 1
        #     j -= 1
        # return value
        new_x = x
        new = 0
        while new_x >0:
            reminder = new_x % 10
            new = (new*10) + reminder
            new_x = new_x // 10
        if new == x:
            return True
        else:
            return False