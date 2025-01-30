class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        new = 0
        while temp:
            new = (new * 10) + (temp % 10)
            temp //= 10
        if new == x:
            return True
        else:
            return False