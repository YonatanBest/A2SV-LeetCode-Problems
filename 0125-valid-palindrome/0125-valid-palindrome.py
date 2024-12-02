class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < len(s) and j >= 0:
            if s[i].isalnum() and s[j].isalnum() and s[i].lower() != s[j].lower():
                return False
            elif not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                i += 1
                j -= 1
        return True