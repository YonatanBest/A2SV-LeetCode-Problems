class Solution:
    def isPalindrome(self, s: str) -> bool:
        checkable = []
        for i in s:
            if i.isalnum():
                checkable.append(i.lower())
        check = list(reversed(checkable))
        if checkable == check:
            return True
        else:
            return False